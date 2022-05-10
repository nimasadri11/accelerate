import setuptools

setuptools.setup(
    name="accelerate_fastai_integration",
    version="0.0.1",
    description="Accelerate fastai integration",
    license="Apache",
    author="The HuggingFace team",
    author_email="zach.mueller@huggingface.co",
    packages=setuptools.find_packages(),
    python_requires=">=3.6.0",
    install_requires=["accelerate", "fastai>=2.0.0"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ]
)