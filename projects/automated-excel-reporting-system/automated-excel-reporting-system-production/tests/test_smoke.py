from pathlib import Path
def test_source_exists():
 assert Path('app.py').exists()
def test_readme_mentions_usage():
 assert 'Usage' in Path('README.md').read_text()
