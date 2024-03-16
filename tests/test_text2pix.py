import pytest
from text2pix import generate_image_from_text

def test_generate_image_from_text_success():
    """Test generating an image with a known text description."""
    text_description = "A beautiful sunrise"
    image_content = generate_image_from_text(text_description)
    assert image_content is not None

def test_generate_image_from_text_failure():
    """Test generating an image with an invalid text description."""
    text_description = ""
    with pytest.raises(Exception) as exc_info:
        generate_image_from_text(text_description)
    assert "Failed to retrieve the image." in str(exc_info.value)
