import streamlit as st
import math

# Page Configuration
st.set_page_config(page_title="Geometry Tuning-In", layout="centered")

st.title("Geometry Tuning-In: The Dimension Jump")
st.write("Welcome to Grade 8 Geometry! Let's bridge the gap from 2D to 3D.")

# Sidebar Navigation
step = st.sidebar.radio("Go to Stage:", ["1. Extrusion (2D to 3D)", "2. Volume Mystery", "3. Cross-Section Detective", "4. Pattern Recognition"])

# --- STAGE 1: EXTRUSION ---
if step == "1. Extrusion (2D to 3D)":
    st.header("Stage 1: From Flat to Solid")
    st.write("In Grade 7, you mastered Area. Now, let's see how Volume works.")
    
    shape_type = st.selectbox("Choose a Base Shape:", ["Rectangle", "Circle"])
    height = st.slider("Extrude Height (cm):", 0, 100, 0)
    
    st.write("---")
    
    if shape_type == "Rectangle":
        length = 10
        width = 6
        base_area = length * width
        volume = base_area * height
        
        # Simple SVG visualization for Rectangle/Prism
        # Note: Streamlit renders HTML/SVG using st.markdown with unsafe_allow_html
        svg_code = f"""
        <svg width="300" height="300">
            <rect x="50" y="{200 - height}" width="150" height="80" fill="#3498db" stroke="black" stroke-width="2" opacity="0.7"/>
            <rect x="50" y="200" width="150" height="80" fill="none" stroke="black" stroke-width="2" stroke-dasharray="4"/>
            <line x1="50" y1="200" x2="50" y2="{200 - height}" stroke="black" stroke-width="2"/>
            <line x1="200" y1="200" x2="200" y2="{200 - height}" stroke="black" stroke-width="2"/>
            <text x="125" y="290" text-anchor="middle" font-family="Arial">Base Area = {base_area} cm²</text>
        </svg>
        """
        st.markdown(svg_code, unsafe_allow_html=True)
        
        if height > 0:
            st.success(f"🎉 You created a **Rectangular Prism**!")
            st.metric(label="Volume (Base Area × Height)", value=f"{volume} cm³")
        else:
            st.info("Move the slider to give the rectangle height!")

    elif shape_type == "Circle":
        radius = 5
        base_area = round(math.pi * radius**2, 2)
        volume = round(base_area * height, 2)
        
        svg_code = f"""
        <svg width="300" height="300">
            <ellipse cx="150" cy="{200 - height}" rx="70" ry="20" fill="#e67e22" stroke="black" stroke-width="2" opacity="0.7"/>
            <ellipse cx="150" cy="200" rx="70" ry="20" fill="none" stroke="black" stroke-width="2" stroke-dasharray="4"/>
            <line x1="80" y1="200" x2="80" y2="{200 - height}" stroke="black" stroke-width="2"/>
            <line x1="220" y1="200" x2="220" y2="{200 - height}" stroke="black" stroke-width="2"/>
            <text x="150" y="250" text-anchor="middle" font-family="Arial">Base Area ≈ {base_area} cm²</text>
        </svg>
        """
        st.markdown(svg_code, unsafe_allow_html=True)
        
        if height > 0:
            st.success(f"🎉 You created a **Cylinder**!")
            st.metric(label="Volume", value=f"{volume} cm³")

# --- STAGE 2: VOLUME MYSTERY ---
elif step == "2. Volume Mystery":
    st.header("Stage 2: Cone vs. Cylinder")
    st.write("Imagine a Cylinder and a Cone with the **same radius** and **same height**.")
    
    guess = st.radio("How many cones full of water does it take to fill the cylinder?", [1, 2, 3, 4])
    
    if st.button("Check Answer"):
        if guess == 3:
            st.balloons()
            st.success("Correct! The volume of a cone is exactly 1/3 of a cylinder.")
            st.latex(r"V_{cone} = \frac{1}{3} \pi r^2 h")
        else:
            st.error("Not quite. Try visualizing it again!")

# --- STAGE 3: CROSS SECTIONS ---
elif step == "3. Cross-Section Detective":
    st.header("Stage 3: Slicing Shapes")
    st.write("If you slice a 3D object, you get a 2D cross-section.")
    
    st.subheader("Case 1: The Square Pyramid")
    st.write("Imagine slicing a Square Pyramid horizontally (parallel to the base).")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Static Pyramid SVG
        st.markdown("""
        <svg width="200" height="200">
            <polygon points="100,20 40,180 160,180" fill="none" stroke="#2c3e50" stroke-width="2"/>
            <line x1="100" y1="20" x2="100" y2="180" stroke="#e74c3c" stroke-dasharray="4"/>
            <line x1="40" y1="180" x2="160" y2="180" stroke="#2c3e50" stroke-width="2"/>
            <line x1="40" y1="180" x2="80" y2="140" stroke="#ccc" stroke-dasharray="4"/>
            <line x1="160" y1="180" x2="120" y2="140" stroke="#ccc" stroke-dasharray="4"/>
            <line x1="100" y1="20" x2="80" y2="140" stroke="#ccc" stroke-dasharray="4"/>
            <line x1="20" y1="100" x2="180" y2="100" stroke="#e67e22" stroke-width="3" stroke-dasharray="5,5"/>
            <text x="185" y="105" fill="#e67e22" font-size="12">Cut Line</text>
        </svg>
        """, unsafe_allow_html=True)

    with col2:
        cs_guess = st.selectbox("What shape do you see?", ["Triangle", "Circle", "Square", "Trapezoid"])
        
        if st.button("Reveal Evidence"):
            if cs_guess == "Square":
                st.success("Correct! It is a smaller square.")
                # Show Square SVG
                st.markdown("""
                <div style="text-align:center;">
                    <svg width="100" height="100">
                        <rect x="25" y="25" width="50" height="50" fill="#2ecc71" stroke="black" stroke-width="2"/>
                        <text x="50" y="90" text-anchor="middle" font-size="12">Cross Section</text>
                    </svg>
                </div>
                """, unsafe_allow_html=True)
            elif cs_guess == "Triangle":
                st.warning("Incorrect. A triangle would be a vertical slice through the apex.")
                # Show Triangle SVG
                st.markdown("""
                <div style="text-align:center;">
                    <svg width="100" height="100">
                        <polygon points="50,10 10,90 90,90" fill="#e74c3c" stroke="black" stroke-width="2"/>
                        <text x="50" y="98" text-anchor="middle" font-size="10">(Vertical Slice)</text>
                    </svg>
                </div>
                """, unsafe_allow_html=True)
            elif cs_guess == "Circle":
                st.warning("Incorrect. A circle comes from slicing a Cone or Sphere.")
                # Show Circle SVG
                st.markdown("""
                <div style="text-align:center;">
                    <svg width="100" height="100">
                        <circle cx="50" cy="50" r="30" fill="#e74c3c" stroke="black" stroke-width="2"/>
                    </svg>
                </div>
                """, unsafe_allow_html=True)
            elif cs_guess == "Trapezoid":
                st.warning("Incorrect. A trapezoid comes from slicing a Pyramid at an angle, or a Prism.")
                # Show Trapezoid SVG
                st.markdown("""
                <div style="text-align:center;">
                    <svg width="100" height="100">
                        <polygon points="30,30 70,30 90,80 10,80" fill="#e74c3c" stroke="black" stroke-width="2"/>
                    </svg>
                </div>
                """, unsafe_allow_html=True)

# --- STAGE 4: PATTERNS ---
elif step == "4. Pattern Recognition":
    st.header("Stage 4: Arithmetic Sequences")
    st.write("Geometry often follows patterns. Let's look at Surface Area.")
    
    st.info("1 Cube = 6 cm² SA \n\n 2 Cubes (stacked) = 10 cm² SA \n\n 3 Cubes (stacked) = 14 cm² SA")
    
    user_val = st.number_input("Predict the Surface Area for 10 stacked cubes:", min_value=0)
    
    if st.button("Verify Pattern"):
        # Pattern is 4n + 2
        correct_val = 4 * 10 + 2
        if user_val == correct_val:
            st.success(f"Excellent! The answer is {correct_val} cm².")
            st.write("The rule is: Start with 6, add 4 for every new cube.")
        else:
            st.error("Check the pattern again. How much does it go up by each time?")
