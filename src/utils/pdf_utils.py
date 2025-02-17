def split_pdf_to_images(pdf_path: str, output_dir: str) -> None:
    from pdf2image import convert_from_path
    import os

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f'page_{i + 1}.png')
        image.save(image_path, 'PNG')