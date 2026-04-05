import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Treasure Island", page_icon="🏝️")

# --- INITIALIZE GAME STATE ---
if "stage" not in st.session_state:
    st.session_state.stage = "start"

# --- THE GAME LOGIC ---
st.title("🏝️ Treasure Island")

if st.session_state.stage == "start":
    # 1. Add the image
    st.image("https://images.unsplash.com/photo-1519114056088-b877fe073a5e?q=80&w=1000&auto=format&fit=crop",
             caption="The adventure begins...",
             use_container_width=True)

    # 2. Add the text (Only once!)
    st.subheader("Welcome to Treasure Island!")
    st.write("Your mission is to find the treasure. You're at a crossroad. Where do you want to go?")

    # 3. Create the buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Go Left"):
            st.session_state.stage = "lake"
            st.rerun()
    with col2:
        if st.button("Go Right"):
            st.session_state.stage = "hole_over"
            st.rerun()


elif st.session_state.stage == "lake":
    st.write("🌊 You've come to a lake. There is an island in the middle.")
    col1, col2 = st.columns(2)
    if col1.button("Wait for boat"):
        st.session_state.stage = "house"
        st.rerun()
    if col2.button("Swim across"):
        # 50/50 chance of survival
        if random.choice([True, False]):
            st.session_state.stage = "trout_over"
        else:
            st.success("You swam like a pro!")
            st.session_state.stage = "house"
        st.rerun()

elif st.session_state.stage == "house":
    st.write("🏡 You've arrived at the island. There is a house with three doors.")
    c1, c2, c3 = st.columns(3)
    if c1.button("🔴 Red"):
        st.session_state.stage = "fire_over"
        st.rerun()
    if c2.button("🟡 Yellow"):
        st.session_state.stage = "win"
        st.rerun()
    if c3.button("🔵 Blue"):
        st.session_state.stage = "beast_over"
        st.rerun()

# --- ENDINGS ---
elif st.session_state.stage == "win":
    st.balloons()
    st.success("💰 You found the treasure! YOU WIN!")
    if st.button("Play Again"):
        st.session_state.stage = "start"
        st.rerun()

else:
    st.error("Game Over!")
    if st.session_state.stage == "hole_over":
        st.write("You fell into a hole. Watch your step next time!")
    elif st.session_state.stage == "trout_over":
        st.write("Attacked by angry trouts. They were hungry!")
    elif st.session_state.stage == "fire_over":
        st.write("Room full of fire. Toasty!")
    elif st.session_state.stage == "beast_over":
        st.write("Room full of beasts. Better luck next time!")

    if st.button("Restart"):
        st.session_state.stage = "start"
        st.rerun()