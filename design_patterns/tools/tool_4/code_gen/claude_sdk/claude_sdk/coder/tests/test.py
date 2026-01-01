import unittest
import os
import sys
import shutil
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from code_generator import code_gen_project, get_output_dir


class TestCodeGenerator(unittest.TestCase):
    """Test cases for the code_gen_project function."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.output_dir = get_output_dir()
        self.test_projects = []
    
    def tearDown(self):
        """Clean up created test projects."""
        for project_name in self.test_projects:
            project_path = self.output_dir / project_name
            if project_path.exists():
                shutil.rmtree(project_path)
    
    def test_code_gen_project_creates_directory(self):
        """Test that code_gen_project creates the project directory."""
        project_name = "test_project_dir"
        self.test_projects.append(project_name)
        
        result_path = code_gen_project("Create a hello world function", project_name)
        
        self.assertTrue(os.path.exists(result_path))
        self.assertTrue(os.path.isdir(result_path))
    
    def test_code_gen_project_creates_src_directory(self):
        """Test that code_gen_project creates src directory."""
        project_name = "test_project_src"
        self.test_projects.append(project_name)
        
        result_path = code_gen_project("Create a greeting function", project_name)
        
        src_path = Path(result_path) / "src"
        self.assertTrue(src_path.exists())
    
    def test_code_gen_project_creates_tests_directory(self):
        """Test that code_gen_project creates tests directory."""
        project_name = "test_project_tests"
        self.test_projects.append(project_name)
        
        result_path = code_gen_project("Create a calculator", project_name)
        
        tests_path = Path(result_path) / "tests"
        self.assertTrue(tests_path.exists())
    
    def test_code_gen_project_creates_readme_files(self):
        """Test that code_gen_project creates README files."""
        project_name = "test_project_readme"
        self.test_projects.append(project_name)
        
        result_path = code_gen_project("Create a utility function", project_name)
        
        readme_api = Path(result_path) / "README_API_SIGNATURE.md"
        readme_tests = Path(result_path) / "README_tests.md"
        
        self.assertTrue(readme_api.exists())
        self.assertTrue(readme_tests.exists())
    
    def test_code_gen_project_returns_absolute_path(self):
        """Test that code_gen_project returns an absolute path."""
        project_name = "test_project_path"
        self.test_projects.append(project_name)
        
        result_path = code_gen_project("Create a simple function", project_name)
        
        self.assertTrue(os.path.isabs(result_path))
    
    def test_code_gen_fibonacci_project(self):
        """Test generating a fibonacci project with actual code."""
        project_name = "fibonacci_generated"
        self.test_projects.append(project_name)
        
        result_path = code_gen_project(
            "Create a function that calculates fibonacci numbers",
            project_name
        )
        
        # Check that code was generated
        src_path = Path(result_path) / "src"
        code_files = list(src_path.glob("*.py"))
        self.assertTrue(len(code_files) > 0)
        
        # Check that the code contains fibonacci-related content
        for code_file in code_files:
            if code_file.name != "__init__.py":
                content = code_file.read_text()
                self.assertIn("def", content)  # Has function definitions
    
    def test_code_gen_calculator_project(self):
        """Test generating a calculator project with actual code."""
        project_name = "calculator_generated"
        self.test_projects.append(project_name)
        
        result_path = code_gen_project(
            "Create a simple calculator with add, subtract, multiply, divide",
            project_name
        )
        
        # Check that code was generated
        src_path = Path(result_path) / "src"
        code_files = [f for f in src_path.glob("*.py") if f.name != "__init__.py"]
        self.assertTrue(len(code_files) > 0)
        
        # Check test file exists
        tests_path = Path(result_path) / "tests"
        test_files = list(tests_path.glob("test_*.py"))
        self.assertTrue(len(test_files) > 0)
    
    def test_code_gen_project_runs_tests(self):
        """Test that code_gen_project runs tests and creates result file."""
        project_name = "test_project_run_tests"
        self.test_projects.append(project_name)
        
        result_path = code_gen_project(
            "Create a hello world greeting function",
            project_name
        )
        
        result_file = Path(result_path) / "test_result.txt"
        self.assertTrue(result_file.exists())
        
        content = result_file.read_text()
        self.assertIn("Test Result:", content)


class TestCodeGeneratorIntegration(unittest.TestCase):
    """Integration tests that generate actual projects for inspection."""
    
    def test_generate_persistent_fibonacci_project(self):
        """Generate a fibonacci project that persists for inspection."""
        project_name = "demo_fibonacci_project"
        
        result_path = code_gen_project(
            "Create a function that calculates fibonacci numbers",
            project_name
        )
        
        print(f"\nGenerated fibonacci project at: {result_path}")
        
        # Verify structure
        project_path = Path(result_path)
        self.assertTrue((project_path / "src").exists())
        self.assertTrue((project_path / "tests").exists())
        self.assertTrue((project_path / "README_API_SIGNATURE.md").exists())
        self.assertTrue((project_path / "README_tests.md").exists())
        
        # Print generated code for inspection
        src_files = list((project_path / "src").glob("*.py"))
        for f in src_files:
            if f.name != "__init__.py":
                print(f"\n--- Generated code in {f.name} ---")
                print(f.read_text()[:500])  # First 500 chars
    
    def test_generate_persistent_calculator_project(self):
        """Generate a calculator project that persists for inspection."""
        project_name = "demo_calculator_project"
        
        result_path = code_gen_project(
            "Create a simple calculator with add, subtract, multiply, divide functions",
            project_name
        )
        
        print(f"\nGenerated calculator project at: {result_path}")
        
        # Verify test results
        result_file = Path(result_path) / "test_result.txt"
        if result_file.exists():
            print(f"\n--- Test Results ---")
            print(result_file.read_text()[:1000])


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    replay_dir = Path(__file__).parent.parent / "replay"
    replay_dir.mkdir(exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestCodeGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestCodeGeneratorIntegration))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open(replay_dir / 'test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
