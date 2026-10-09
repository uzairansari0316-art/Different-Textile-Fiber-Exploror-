import streamlit as st

st.set_page_config(
    page_title="Textile Fiber Explorer",
    page_icon="🧵",
    layout="wide"
)

st.title("🧵 Textile Fiber Explorer")
st.write("Learn about textile fibers, their properties, and applications.")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox(
    "Choose a Section",
    ["Home", "Fiber Information", "Compare Fibers", "About"]
)

fibers = {
    "Cotton": {
        "Category": "Natural - Vegetable",
        "Source": "Cotton plant",
        "Properties": "Soft, breathable, absorbent, comfortable",
        "Uses": "Clothing, bedsheets, towels",
        "Advantages": "Comfortable, absorbent, easy to dye"
    },
    "Wool": {
        "Category": "Natural - Animal",
        "Source": "Sheep fleece",
        "Properties": "Warm, elastic, moisture-absorbing",
        "Uses": "Sweaters, coats, blankets",
        "Advantages": "Good insulation, elastic, warm"
    },
    "Silk": {
        "Category": "Natural - Animal",
        "Source": "Silkworm cocoons",
        "Properties": "Smooth, lustrous, fine, strong",
        "Uses": "Luxury clothing, scarves, dresses",
        "Advantages": "Attractive shine, soft feel"
    },
    "Polyester": {
        "Category": "Synthetic",
        "Source": "Petroleum-based chemicals",
        "Properties": "Strong, wrinkle-resistant, quick-drying",
        "Uses": "Sportswear, shirts, curtains",
        "Advantages": "Durable, easy-care, quick-drying"
    },
    "Nylon": {
        "Category": "Synthetic",
        "Source": "Synthetic polymers",
        "Properties": "Strong, lightweight, abrasion-resistant",
        "Uses": "Sportswear, ropes, hosiery",
        "Advantages": "High strength, lightweight, durable"
    },
    "Rayon": {
        "Category": "Regenerated cellulose",
        "Source": "Processed plant cellulose",
        "Properties": "Soft, absorbent, good drape",
        "Uses": "Dresses, linings, shirts",
        "Advantages": "Comfortable, soft, drapes well"
    }
}

if page == "Home":
    st.header("Welcome to Textile Fiber Explorer")
    st.write(
        "This application helps students understand textile fibers, "
        "their sources, properties, and uses in the textile industry."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Fibers Available", len(fibers))
    col2.metric("Natural Fibers", 3)
    col3.metric("Synthetic Fibers", 2)

    st.subheader("What is a Textile Fiber?")
    st.write(
        "A textile fiber is a thin, flexible material that can be spun "
        "into yarn and used to manufacture fabrics."
    )

    st.subheader("Fiber Categories")
    st.markdown("""
    - **Natural fibers:** Cotton, wool, silk
    - **Synthetic fibers:** Polyester, nylon
    - **Regenerated fibers:** Rayon
    """)

elif page == "Fiber Information":
    st.header("Fiber Information")

    search = st.text_input("Search for a fiber")
    available_fibers = [
        fiber for fiber in fibers
        if search.lower() in fiber.lower()
    ]

    if available_fibers:
        selected_fiber = st.selectbox(
            "Select a Textile Fiber",
            available_fibers
        )

        details = fibers[selected_fiber]
        st.subheader(selected_fiber)

        st.write("**Category:**", details["Category"])
        st.write("**Source:**", details["Source"])
        st.write("**Properties:**", details["Properties"])
        st.write("**Uses:**", details["Uses"])
        st.write("**Advantages:**", details["Advantages"])
    else:
        st.warning("No fiber found. Try another name.")

elif page == "Compare Fibers":
    st.header("Compare Textile Fibers")

    fiber1 = st.selectbox("First Fiber", list(fibers.keys()))
    fiber2 = st.selectbox(
        "Second Fiber",
        list(fibers.keys()),
        index=1
    )

    if fiber1 == fiber2:
        st.info("Select two different fibers for comparison.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(fiber1)
            for key, value in fibers[fiber1].items():
                st.write(f"**{key}:** {value}")

        with col2:
            st.subheader(fiber2)
            for key, value in fibers[fiber2].items():
                st.write(f"**{key}:** {value}")

elif page == "About":
    st.header("About This Application")
    st.write(
        "Textile Fiber Explorer is an educational application "
        "designed for textile engineering students."
    )
    st.write("**Technology:** Python and Streamlit")
    st.write("**Purpose:** Learning about textile fibers and their applications.")

st.divider()
st.caption("Textile Fiber Explorer | Educational Project")
