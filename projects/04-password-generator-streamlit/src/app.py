from pathlib import Path

import streamlit as st

from password_generator import (
    MemorablePasswordGenerator,
    PinCodeGenerator,
    RandomPasswordGenerator,
)

BANNER_PATH = Path(__file__).parent / "images" / "banner.jpeg"

st.set_page_config(page_title="Password Generator", page_icon="🔐")
st.image(BANNER_PATH, width=2000)
st.title("⚡ Password Generator")

option = st.radio(
    "Select a password generator",
    ("Random", "Memorable", "PIN Code"),
)

if option == "PIN Code":
    length = st.slider("Select the PIN length", 4, 32)
    generator = PinCodeGenerator(length)

elif option == "Random":
    length = st.slider("Select the password length", 8, 100)
    include_symbols = st.toggle("Include symbols")
    include_numbers = st.toggle("Include numbers")

    generator = RandomPasswordGenerator(
        length=length,
        include_numbers=include_numbers,
        include_symbols=include_symbols,
    )

else:
    number_of_words = st.slider("Select the number of words", 1, 10)
    separator = st.text_input("Separator", value="_")
    capitalization = st.toggle("Capitalization")

    generator = MemorablePasswordGenerator(
        no_of_words=number_of_words,
        separator=separator,
        capitalization=capitalization,
    )

password = generator.generate()
st.write(f"Generated Password: `{password}`")
