import streamlit as st
import time
import random

def load_css(file_name="style.css"):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def render_glitch_header(text, subtext=""):
    st.markdown(f"""<div style="text-align: center; margin-bottom: 40px;">
<h1 class="glitch-text" style="font-size: 3em; margin: 0;">{text}</h1>
<p class="neon-green" style="font-size: 1.2em; letter-spacing: 2px;">{subtext}</p>
</div>""", unsafe_allow_html=True)

def render_glass_card(content):
    st.markdown(f"""<div class="glass-card">
{content}
</div>""", unsafe_allow_html=True)

def render_resonance_meter(protons, electrons, neutrals=0):
    total = protons + electrons + neutrals
    if total == 0:
        position = 50 # Center
    else:
        # Calculate balance: -100 (Pure Electron) to +100 (Pure Proton)
        balance = ((protons - electrons) / total) * 50 # Scale to +/- 50
        position = 50 + balance # Shift from center (50)
    
    # Clamp
    position = max(5, min(95, position))
    
    st.markdown(f"""<div class="meter-wrapper">
<div class="meter-scale">
<div class="scale-red"></div>
<div class="scale-grey"></div>
<div class="scale-green"></div>
</div>
<div class="meter-needle" style="left: {position}%;"></div>
</div>
<div style="display: flex; justify-content: space-between; font-size: 0.8em; color: #888; margin-top: 5px;">
<span>UNSTABLE</span>
<span>NEUTRAL</span>
<span>STABLE</span>
</div>""", unsafe_allow_html=True)

def render_nav_link(label, active=False):
    active_class = "active" if active else ""
    return f'<div class="nav-link {active_class}">{label}</div>'

def render_entanglement_alert(matched_users):
    users_str = ", ".join(matched_users)
    st.markdown(f"""<div style="
position: fixed; top: 15%; left: 5%; right: 5%; 
background: rgba(0,0,0,0.95); border: 2px solid #00FF41; 
z-index: 9999; padding: 40px; text-align: center;
box-shadow: 0 0 50px #00FF41;
animation: glitch 0.5s infinite;">
<h1 class="neon-green" style="font-size: 3em;">⚠ QUANTUM ENTANGLEMENT DETECTED ⚠</h1>
<p style="color: #FFF; font-size: 1.5em;">SYNC ESTABLISHED WITH: {users_str}</p>
<p style="color: #888;">THE FOLD IS OPENING...</p>
<p style="font-size: 0.8em; color: #555;">(Click 'ACKNOWLEDGE' below to stabilize)</p>
</div>""", unsafe_allow_html=True)

def render_terminal_boot():
    """Simulates a boot sequence with scrolling text"""
    lines = [
        "INITIALIZING KERNEL...",
        "LOADING REALITY DRIVERS...",
        "BYPASSING SECURITY PROTOCOLS...",
        "CONNECTING TO WORLD LINE 0.00%...",
        "SYNCING WITH QUANTUM SERVER...",
        "DECRYPTING USER DATA...",
        "SYSTEM INTEGRITY: 48%... 72%... 99%...",
        "BREACH DETECTED.",
        "WELCOME TO THE DECOHERENCE LOG."
    ]
    placeholder = st.empty()
    text_buffer = ""
    for line in lines:
        text_buffer += f"> {line}<br>"
        placeholder.markdown(f"""<div class="terminal-text">
{text_buffer}
<span class="cursor"></span>
</div>""", unsafe_allow_html=True)
        time.sleep(0.3)
    
    return placeholder

def get_logo_svg(size=40):
    """
    Returns the SVG code for 'The Split Atom' logo.
    Concept: An atom with a split nucleus, leaking data bits.
    """
    return f"""<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
<defs>
<filter id="glow">
<feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
<feMerge>
<feMergeNode in="coloredBlur"/>
<feMergeNode in="SourceGraphic"/>
</feMerge>
</filter>
</defs>
<!-- Electron Orbits -->
<ellipse cx="50" cy="50" rx="40" ry="10" stroke="#00FF41" stroke-width="1.5" fill="none" transform="rotate(45 50 50)" opacity="0.8" />
<ellipse cx="50" cy="50" rx="40" ry="10" stroke="#00FF41" stroke-width="1.5" fill="none" transform="rotate(-45 50 50)" opacity="0.8" />
<ellipse cx="50" cy="50" rx="40" ry="10" stroke="#00FF41" stroke-width="1.5" fill="none" opacity="0.5" />
<!-- The Split Nucleus -->
<path d="M 50 35 L 50 65" stroke="#000" stroke-width="4" /> <!-- Split Line -->
<!-- Left Hemisphere -->
<path d="M 46 35 A 15 15 0 0 0 46 65" fill="#00FF41" filter="url(#glow)">
<animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite" />
</path>
<!-- Right Hemisphere (Drifting/Decohering) -->
<path d="M 54 35 A 15 15 0 0 1 54 65" fill="#00FF41" filter="url(#glow)" transform="translate(2,0)">
<animateTransform attributeName="transform" type="translate" values="2,0; 4,0; 2,0" dur="0.1s" repeatCount="indefinite" />
</path>
<!-- Data Particles (Leaking) -->
<rect x="55" y="40" width="2" height="2" fill="#FFF" opacity="0.8" />
<rect x="60" y="45" width="2" height="2" fill="#FFF" opacity="0.6" />
<rect x="58" y="55" width="2" height="2" fill="#FFF" opacity="0.9" />
</svg>"""
