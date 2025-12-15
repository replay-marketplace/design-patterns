# Regeneration Prompt for Voice One-Shot Application

Create a Flask web application with the following specifications:

## Project Structure

Create a Flask application with the following file structure:
```
code/v0.1/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Requirements (requirements.txt)

```
flask>=3.0.0
openai>=1.0.0
anthropic>=0.18.0
```

## Flask Application (app.py)

Create a Flask application with the following features:

### Environment Setup
- Initialize OpenAI client using `OPENAI_API_KEY` environment variable (optional, can be None if not set)
- Initialize Anthropic client using `ANTHROPIC_API_KEY` environment variable (optional, can be None if not set)

### Routes

1. **GET `/`** - Main page that renders `index.html`

2. **POST `/button1`** - Record audio and transcribe with OpenAI
   - Accepts audio file in request.files['audio']
   - Saves audio to temporary file
   - Uses OpenAI Whisper API (model: "whisper-1") to transcribe
   - Returns JSON with status, message, and transcribed text
   - Cleans up temporary file after processing
   - Handles errors gracefully with appropriate error messages

3. **POST `/button2`** - Send transcribed text to Anthropic
   - Accepts JSON with 'text' field containing transcribed text
   - Sends text to Anthropic Claude (model: "claude-sonnet-4-5-20250929", max_tokens: 1024)
   - Returns JSON with status, message, and response text
   - Validates that text exists before processing
   - Handles errors gracefully

4. **POST `/button3`** - Create new folder in projects directory
   - Accepts JSON with 'folderName' field
   - Sanitizes folder name (removes invalid characters: < > : " / \ | ? *)
   - Creates 'projects' directory relative to app.py if it doesn't exist
   - Creates new folder inside projects directory
   - Returns error if folder already exists
   - Returns JSON with status and message

5. **POST `/button4` through `/button10`** - Placeholder handlers
   - Each returns JSON: `{'status': 'success', 'message': 'Button X clicked'}`
   - Include TODO comments for future implementation

### Error Handling
- All routes should have try-except blocks
- Return appropriate HTTP status codes (400 for bad requests, 500 for server errors)
- Print errors to console for debugging
- Return user-friendly error messages in JSON responses

### Server Configuration
- Run on port 5000
- Enable debug mode

## HTML Template (templates/index.html)

Create a modern, beautiful web interface with:

### Design
- Gradient background (purple/blue: #667eea to #764ba2)
- White container with rounded corners and shadow
- Modern, clean typography using system fonts
- Responsive design with padding

### UI Elements
- Title: "Button Interface"
- 10 buttons arranged in a vertical grid:
  1. "Record" button (for audio recording)
  2. "Send Prompt" button (for sending to Anthropic)
  3. "Make New Project" button with text input field for folder name
  4-10. "Button 4" through "Button 10" (labeled as such)

### JavaScript Functionality

#### Audio Recording (Button 1)
- Use MediaRecorder API to record audio
- Support start/stop recording (toggle on button click)
- Record in webm format with opus codec
- Button text changes: "Record" → "Stop Recording" → "Processing..."
- Send recorded audio blob to `/button1` endpoint as FormData
- Store transcribed text in variable `transcribedText` for use by button 2
- Display transcription result in status area

#### Send to Anthropic (Button 2)
- Send stored `transcribedText` to `/button2` endpoint as JSON
- Display Anthropic response in status area
- Show error if no transcribed text is available

#### Create Folder (Button 3)
- Get folder name from input field
- Send folder name to `/button3` endpoint as JSON
- Validate that folder name is not empty
- Display success/error message

#### Other Buttons (4-10)
- Send POST request to respective endpoint
- Display response message

### Status Display
- Status div that shows success (green) or error (red) messages
- Clear visual feedback for all operations
- Disable buttons during processing to prevent double-clicks

### Styling Details
- Buttons: gradient background matching page, hover effects, shadow, rounded corners
- Input field: border styling, focus state with purple border
- Status messages: colored backgrounds (green for success, red for error)
- Smooth transitions and animations
- Button-with-input layout: flexbox with button and input side-by-side

## README.md

Include setup instructions:
```markdown
# Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open http://localhost:5000
```

## Key Implementation Details

1. **Audio Handling**: The frontend records audio as webm, sends it to the backend which saves it temporarily, processes with OpenAI Whisper, then deletes the temp file.

2. **Text Flow**: Button 1 transcribes audio and stores text in frontend variable. Button 2 uses that stored text to send to Anthropic.

3. **Folder Creation**: Button 3 creates folders in a `projects/` directory relative to the app.py file location. Folder names are sanitized to prevent directory traversal attacks.

4. **Error Handling**: All endpoints check for required data, validate inputs, check for API key configuration, and return appropriate error messages.

5. **UI/UX**: Modern gradient design, clear button labels, status feedback, disabled states during processing, and responsive layout.

## Environment Variables Required

- `OPENAI_API_KEY` (optional, but required for button 1 functionality)
- `ANTHROPIC_API_KEY` (optional, but required for button 2 functionality)

Generate the complete application with all these specifications.

