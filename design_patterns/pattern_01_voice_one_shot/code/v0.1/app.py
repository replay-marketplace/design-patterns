from flask import Flask, render_template, jsonify, request
import os
import tempfile
import re
import random
import sys
from pathlib import Path
from openai import OpenAI
from anthropic import Anthropic
from python_tools_utils import add_numbers

# Add path to save_text module
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'python_tools', 'save_text_to_md_file'))
from save_text import generate_timestamp_filename

app = Flask(__name__)

# Initialize OpenAI client (will use OPENAI_API_KEY from environment)
client = OpenAI() if os.getenv('OPENAI_API_KEY') else None

# Initialize Anthropic client (will use ANTHROPIC_API_KEY from environment)
anthropic_client = Anthropic() if os.getenv('ANTHROPIC_API_KEY') else None

@app.route('/')
def index():
    """Main page with 10 buttons"""
    return render_template('index.html')

@app.route('/button1', methods=['POST'])
def button1_handler():
    """Handle button 1: Record audio, transcribe with OpenAI"""
    try:
        # Check if audio file is in the request
        if 'audio' not in request.files:
            return jsonify({'status': 'error', 'message': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        
        if audio_file.filename == '':
            return jsonify({'status': 'error', 'message': 'No audio file selected'}), 400
        
        # Check if OpenAI client is initialized
        if client is None:
            return jsonify({'status': 'error', 'message': 'OpenAI API key not configured. Please set OPENAI_API_KEY environment variable.'}), 500
        
        # Save audio to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            audio_file.save(tmp_file.name)
            tmp_path = tmp_file.name
        
        try:
            # Transcribe audio using OpenAI
            with open(tmp_path, 'rb') as audio:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio,
                    response_format="text"
                )
            
            # Print the transcribed text
            print(f"Transcribed text: {transcript}")
            
            # Automatically save transcribed text to markdown file
            try:
                # Generate timestamp-based filename
                filename = generate_timestamp_filename()
                
                # Get the directory where app.py is located
                app_dir = os.path.dirname(os.path.abspath(__file__))
                # Create output directory relative to app directory
                output_dir = Path(app_dir) / 'output'
                output_dir.mkdir(parents=True, exist_ok=True)
                
                # Save the file
                file_path = output_dir / filename
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(transcript)
                
                print(f"✅ Text saved successfully to {file_path}")
            except Exception as save_error:
                # Log the error but don't fail the request
                print(f"Warning: Failed to save transcript to file: {str(save_error)}")
            
            return jsonify({
                'status': 'success', 
                'message': 'Audio transcribed successfully',
                'text': transcript
            })
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
                
    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        return jsonify({'status': 'error', 'message': f'Error processing audio: {str(e)}'}), 500

@app.route('/button2', methods=['POST'])
def button2_handler():
    """Handle button 2: Send transcribed text to Anthropic and get response"""
    try:
        # Get the transcribed text from request
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'status': 'error', 'message': 'No text provided. Please record audio first using Button 1.'}), 400
        
        transcribed_text = data['text']
        
        if not transcribed_text or not transcribed_text.strip():
            return jsonify({'status': 'error', 'message': 'Transcribed text is empty. Please record audio first.'}), 400
        
        # Check if Anthropic client is initialized
        if anthropic_client is None:
            return jsonify({'status': 'error', 'message': 'Anthropic API key not configured. Please set ANTHROPIC_API_KEY environment variable.'}), 500
        
        # Send prompt to Anthropic
        message = anthropic_client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": transcribed_text}
            ]
        )
        
        # Extract response text
        response_text = message.content[0].text
        
        # Print the response
        print(f"Anthropic response: {response_text}")
        
        # Save both input prompt and output response to markdown file
        try:
            # Generate timestamp-based filename
            filename = generate_timestamp_filename()
            
            # Get the directory where app.py is located
            app_dir = os.path.dirname(os.path.abspath(__file__))
            # Create output directory relative to app directory
            output_dir = Path(app_dir) / 'output'
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Format the content with both input and output
            content = f"# Input Prompt\n\n{transcribed_text}\n\n---\n\n# Anthropic Response\n\n{response_text}\n"
            
            # Save the file
            file_path = output_dir / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Input prompt and response saved successfully to {file_path}")
        except Exception as save_error:
            # Log the error but don't fail the request
            print(f"Warning: Failed to save prompt and response to file: {str(save_error)}")
        
        return jsonify({
            'status': 'success',
            'message': 'Anthropic response received',
            'response': response_text
        })
        
    except Exception as e:
        print(f"Error processing Anthropic request: {str(e)}")
        return jsonify({'status': 'error', 'message': f'Error processing request: {str(e)}'}), 500

@app.route('/button3', methods=['POST'])
def button3_handler():
    """Handle button 3: Create a new folder in /projects with the name from text box"""
    try:
        # Get the folder name from request
        data = request.get_json()
        if not data or 'folderName' not in data:
            return jsonify({'status': 'error', 'message': 'No folder name provided.'}), 400
        
        folder_name = data['folderName'].strip()
        
        if not folder_name:
            return jsonify({'status': 'error', 'message': 'Folder name cannot be empty.'}), 400
        
        # Sanitize folder name to prevent directory traversal
        # Remove any path separators and invalid characters
        folder_name = re.sub(r'[<>:"/\\|?*]', '', folder_name)
        folder_name = folder_name.strip()
        
        if not folder_name:
            return jsonify({'status': 'error', 'message': 'Invalid folder name. Please use only valid characters.'}), 400
        
        # Create projects directory relative to the app directory if it doesn't exist
        # Get the directory where app.py is located
        app_dir = os.path.dirname(os.path.abspath(__file__))
        projects_dir = os.path.join(app_dir, 'projects')
        
        if not os.path.exists(projects_dir):
            os.makedirs(projects_dir)
        
        # Create the new folder
        new_folder_path = os.path.join(projects_dir, folder_name)
        
        if os.path.exists(new_folder_path):
            return jsonify({'status': 'error', 'message': f'Folder "{folder_name}" already exists.'}), 400
        
        os.makedirs(new_folder_path)
        
        print(f"Created folder: {new_folder_path}")
        
        return jsonify({
            'status': 'success',
            'message': f'Folder "{folder_name}" created successfully in projects/'
        })
        
    except Exception as e:
        print(f"Error creating folder: {str(e)}")
        return jsonify({'status': 'error', 'message': f'Error creating folder: {str(e)}'}), 500

@app.route('/button4', methods=['POST'])
def button4_handler():
    """Handle button 4: Generate two random numbers and add them using python_tools/add_two_numbers"""
    try:
        # Generate two random numbers
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        # Call the add_numbers function from python_tools_utils
        result = add_numbers(num1, num2)
        
        # Print the output
        print(f"Generated random numbers: {num1} and {num2}")
        print(f"Result of add_numbers({num1}, {num2}): {result}")
        
        return jsonify({
            'status': 'success',
            'message': f'Added {num1} + {num2} = {result}',
            'num1': num1,
            'num2': num2,
            'result': result
        })
        
    except Exception as e:
        print(f"Error in button4_handler: {str(e)}")
        return jsonify({'status': 'error', 'message': f'Error processing request: {str(e)}'}), 500

@app.route('/button5', methods=['POST'])
def button5_handler():
    """Handle button 5: Save transcribed text to a markdown file"""
    try:
        # Get the transcribed text from request
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'status': 'error', 'message': 'No text provided. Please record audio first using Button 1.'}), 400
        
        transcribed_text = data['text']
        
        if not transcribed_text or not transcribed_text.strip():
            return jsonify({'status': 'error', 'message': 'Transcribed text is empty. Please record audio first.'}), 400
        
        # Generate timestamp-based filename
        filename = generate_timestamp_filename()
        
        # Get the directory where app.py is located
        app_dir = os.path.dirname(os.path.abspath(__file__))
        # Create output directory relative to app directory
        output_dir = Path(app_dir) / 'output'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save the file
        file_path = output_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(transcribed_text)
        
        print(f"✅ Text saved successfully to {file_path}")
        
        return jsonify({
            'status': 'success',
            'message': f'Prompt saved successfully to {filename}',
            'filename': filename,
            'filepath': str(file_path)
        })
        
    except Exception as e:
        print(f"Error saving prompt: {str(e)}")
        return jsonify({'status': 'error', 'message': f'Error saving prompt: {str(e)}'}), 500

@app.route('/button6', methods=['POST'])
def button6_handler():
    """Placeholder function for button 6"""
    # TODO: Add implementation later
    return jsonify({'status': 'success', 'message': 'Button 6 clicked'})

@app.route('/button7', methods=['POST'])
def button7_handler():
    """Placeholder function for button 7"""
    # TODO: Add implementation later
    return jsonify({'status': 'success', 'message': 'Button 7 clicked'})

@app.route('/button8', methods=['POST'])
def button8_handler():
    """Placeholder function for button 8"""
    # TODO: Add implementation later
    return jsonify({'status': 'success', 'message': 'Button 8 clicked'})

@app.route('/button9', methods=['POST'])
def button9_handler():
    """Placeholder function for button 9"""
    # TODO: Add implementation later
    return jsonify({'status': 'success', 'message': 'Button 9 clicked'})

@app.route('/button10', methods=['POST'])
def button10_handler():
    """Placeholder function for button 10"""
    # TODO: Add implementation later
    return jsonify({'status': 'success', 'message': 'Button 10 clicked'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

