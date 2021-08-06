from setuptools import setup, find_packages

setup(
    name='niaimage2table',
    version='1.0',
    description='Extract text from tables in images.',
    author='Bae Yong Bin',
    author_email='mame-mame@kakao.com',
    url='',
    download_url='',
    install_requires=['numpy', 'torch', 'torchvision', 'opencv-python', 'easyocr'],
    packages=find_packages(),
    keywords=['Extract_text', 'table_ocr', 'easyOCR'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)