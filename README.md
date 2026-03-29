<div align="center">

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                     KURUKSHETRA BANNER                        -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<svg viewBox="0 0 900 280" xmlns="http://www.w3.org/2000/svg" width="100%">
  <defs>
    <!-- Sky gradient: deep twilight -->
    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0a0612"/>
      <stop offset="50%" style="stop-color:#1a0a1f"/>
      <stop offset="100%" style="stop-color:#2d1008"/>
    </linearGradient>
    <!-- Golden glow behind chariot -->
    <radialGradient id="divineLight" cx="52%" cy="60%" r="35%">
      <stop offset="0%" style="stop-color:#c8860a;stop-opacity:0.35"/>
      <stop offset="100%" style="stop-color:#0a0612;stop-opacity:0"/>
    </radialGradient>
    <!-- Ground gradient -->
    <linearGradient id="ground" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#3d1a00"/>
      <stop offset="100%" style="stop-color:#1a0800"/>
    </linearGradient>
    <!-- Wheel glow -->
    <radialGradient id="wheelGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#d4860a;stop-opacity:0.6"/>
      <stop offset="100%" style="stop-color:#d4860a;stop-opacity:0"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- Dust haze at ground -->
    <linearGradient id="dustHaze" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#8B4513;stop-opacity:0"/>
      <stop offset="100%" style="stop-color:#8B4513;stop-opacity:0.25"/>
    </linearGradient>
  </defs>

  <!-- Sky -->
  <rect width="900" height="280" fill="url(#sky)"/>

  <!-- Stars scattered -->
  <circle cx="60" cy="25" r="1" fill="#e8d5a3" opacity="0.6"/>
  <circle cx="130" cy="15" r="0.8" fill="#e8d5a3" opacity="0.5"/>
  <circle cx="210" cy="30" r="1.2" fill="#e8d5a3" opacity="0.7"/>
  <circle cx="290" cy="12" r="0.9" fill="#e8d5a3" opacity="0.4"/>
  <circle cx="380" cy="22" r="1" fill="#e8d5a3" opacity="0.6"/>
  <circle cx="600" cy="18" r="0.8" fill="#e8d5a3" opacity="0.5"/>
  <circle cx="700" cy="28" r="1.1" fill="#e8d5a3" opacity="0.6"/>
  <circle cx="780" cy="10" r="0.7" fill="#e8d5a3" opacity="0.4"/>
  <circle cx="840" cy="35" r="1" fill="#e8d5a3" opacity="0.5"/>
  <circle cx="45" cy="55" r="0.6" fill="#e8d5a3" opacity="0.3"/>
  <circle cx="160" cy="48" r="0.8" fill="#e8d5a3" opacity="0.4"/>
  <circle cx="850" cy="55" r="0.7" fill="#e8d5a3" opacity="0.3"/>

  <!-- Distant army silhouettes — left -->
  <rect x="0" y="185" width="2" height="30" fill="#1a0800" opacity="0.7"/>
  <rect x="8" y="182" width="2" height="33" fill="#1a0800" opacity="0.6"/>
  <rect x="16" y="188" width="2" height="27" fill="#1a0800" opacity="0.5"/>
  <rect x="24" y="184" width="2" height="31" fill="#1a0800" opacity="0.7"/>
  <rect x="32" y="190" width="2" height="25" fill="#1a0800" opacity="0.5"/>
  <rect x="40" y="183" width="2" height="32" fill="#1a0800" opacity="0.6"/>
  <rect x="50" y="187" width="2" height="28" fill="#1a0800" opacity="0.4"/>
  <rect x="60" y="185" width="2" height="30" fill="#1a0800" opacity="0.5"/>
  <rect x="70" y="189" width="2" height="26" fill="#1a0800" opacity="0.4"/>
  <rect x="80" y="184" width="2" height="31" fill="#1a0800" opacity="0.3"/>
  <!-- Distant army silhouettes — right -->
  <rect x="820" y="185" width="2" height="30" fill="#1a0800" opacity="0.7"/>
  <rect x="830" y="182" width="2" height="33" fill="#1a0800" opacity="0.6"/>
  <rect x="840" y="188" width="2" height="27" fill="#1a0800" opacity="0.5"/>
  <rect x="850" y="184" width="2" height="31" fill="#1a0800" opacity="0.7"/>
  <rect x="860" y="190" width="2" height="25" fill="#1a0800" opacity="0.5"/>
  <rect x="870" y="183" width="2" height="32" fill="#1a0800" opacity="0.6"/>
  <rect x="880" y="187" width="2" height="28" fill="#1a0800" opacity="0.4"/>
  <rect x="890" y="185" width="2" height="30" fill="#1a0800" opacity="0.5"/>

  <!-- Divine glow behind scene -->
  <ellipse cx="460" cy="165" rx="200" ry="90" fill="url(#divineLight)"/>

  <!-- Ground — Kurukshetra battlefield earth -->
  <rect x="0" y="215" width="900" height="65" fill="url(#ground)"/>
  <!-- Dust haze at base -->
  <rect x="0" y="200" width="900" height="80" fill="url(#dustHaze)"/>

  <!-- ═══════════ CHARIOT ═══════════ -->
  <!-- Chariot body — ornate golden frame -->
  <rect x="355" y="155" width="175" height="62" rx="5" fill="#1a0a00" stroke="#b8730a" stroke-width="1.5"/>
  <rect x="362" y="162" width="161" height="48" rx="3" fill="#0f0600" stroke="#d4860a" stroke-width="0.8" opacity="0.7"/>
  <!-- Chariot decorative panelling -->
  <line x1="420" y1="155" x2="420" y2="217" stroke="#b8730a" stroke-width="0.6" opacity="0.5"/>
  <line x1="470" y1="155" x2="470" y2="217" stroke="#b8730a" stroke-width="0.6" opacity="0.5"/>
  <line x1="520" y1="155" x2="520" y2="217" stroke="#b8730a" stroke-width="0.6" opacity="0.5"/>
  <!-- Corner ornaments -->
  <circle cx="358" cy="158" r="4" fill="#d4860a" opacity="0.8"/>
  <circle cx="527" cy="158" r="4" fill="#d4860a" opacity="0.8"/>
  <circle cx="358" cy="214" r="4" fill="#d4860a" opacity="0.8"/>
  <circle cx="527" cy="214" r="4" fill="#d4860a" opacity="0.8"/>
  <!-- Chariot axle -->
  <rect x="345" y="210" width="200" height="6" rx="3" fill="#8B5E0A" stroke="#d4860a" stroke-width="0.5"/>

  <!-- Left Wheel -->
  <circle cx="375" cy="222" r="32" fill="none" stroke="#b8730a" stroke-width="2.5"/>
  <circle cx="375" cy="222" r="24" fill="none" stroke="#8B5E0A" stroke-width="1"/>
  <circle cx="375" cy="222" r="8" fill="#d4860a" opacity="0.9"/>
  <circle cx="375" cy="222" r="5" fill="#1a0800"/>
  <!-- Wheel spokes -->
  <line x1="375" y1="190" x2="375" y2="212" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="375" y1="232" x2="375" y2="254" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="343" y1="222" x2="365" y2="222" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="385" y1="222" x2="407" y2="222" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="353" y1="200" x2="368" y2="213" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="382" y1="231" x2="397" y2="244" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="353" y1="244" x2="368" y2="231" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="382" y1="213" x2="397" y2="200" stroke="#b8730a" stroke-width="1.5"/>
  <!-- Wheel glow -->
  <circle cx="375" cy="222" r="35" fill="url(#wheelGlow)" opacity="0.4"/>

  <!-- Right Wheel -->
  <circle cx="510" cy="222" r="32" fill="none" stroke="#b8730a" stroke-width="2.5"/>
  <circle cx="510" cy="222" r="24" fill="none" stroke="#8B5E0A" stroke-width="1"/>
  <circle cx="510" cy="222" r="8" fill="#d4860a" opacity="0.9"/>
  <circle cx="510" cy="222" r="5" fill="#1a0800"/>
  <!-- Spokes -->
  <line x1="510" y1="190" x2="510" y2="212" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="510" y1="232" x2="510" y2="254" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="478" y1="222" x2="500" y2="222" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="520" y1="222" x2="542" y2="222" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="488" y1="200" x2="503" y2="213" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="517" y1="231" x2="532" y2="244" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="488" y1="244" x2="503" y2="231" stroke="#b8730a" stroke-width="1.5"/>
  <line x1="517" y1="213" x2="532" y2="200" stroke="#b8730a" stroke-width="1.5"/>
  <circle cx="510" cy="222" r="35" fill="url(#wheelGlow)" opacity="0.4"/>

  <!-- Flag pole -->
  <line x1="443" y1="65" x2="443" y2="158" stroke="#8B5E0A" stroke-width="2"/>
  <!-- Hanuman flag (triangle) -->
  <polygon points="443,68 443,105 478,86" fill="#8B1A00" opacity="0.9"/>
  <polygon points="443,68 443,105 478,86" fill="none" stroke="#d4860a" stroke-width="0.8"/>

  <!-- Yoke bar connecting to horses -->
  <line x1="355" y1="210" x2="270" y2="205" stroke="#8B5E0A" stroke-width="3"/>
  <line x1="270" y1="205" x2="240" y2="208" stroke="#8B5E0A" stroke-width="2"/>
  <line x1="270" y1="205" x2="240" y2="200" stroke="#8B5E0A" stroke-width="2"/>

  <!-- Horse 1 (left) — white horse silhouette -->
  <ellipse cx="215" cy="207" rx="45" ry="18" fill="#d4d0c8" opacity="0.85"/>
  <circle cx="175" cy="200" r="14" fill="#d4d0c8" opacity="0.85"/>
  <!-- Horse 1 legs -->
  <rect x="185" y="220" width="5" height="22" rx="2" fill="#b8b4ac" opacity="0.8"/>
  <rect x="198" y="222" width="5" height="20" rx="2" fill="#b8b4ac" opacity="0.8"/>
  <rect x="215" y="221" width="5" height="21" rx="2" fill="#b8b4ac" opacity="0.8"/>
  <rect x="228" y="220" width="5" height="22" rx="2" fill="#b8b4ac" opacity="0.8"/>
  <!-- Horse 1 head details -->
  <ellipse cx="166" cy="197" rx="8" ry="10" fill="#d4d0c8" opacity="0.85"/>
  <line x1="165" y1="187" x2="167" y2="175" stroke="#c8c4bc" stroke-width="2"/>
  <!-- Mane -->
  <path d="M168 187 Q175 182 180 195" stroke="#a09c94" stroke-width="1.5" fill="none"/>

  <!-- Horse 2 (right) — white horse silhouette -->
  <ellipse cx="235" cy="200" rx="40" ry="16" fill="#cccac2" opacity="0.8"/>
  <circle cx="198" cy="193" r="12" fill="#cccac2" opacity="0.8"/>
  <!-- Horse 2 legs -->
  <rect x="205" y="212" width="5" height="24" rx="2" fill="#b0aea6" opacity="0.7"/>
  <rect x="218" y="214" width="5" height="22" rx="2" fill="#b0aea6" opacity="0.7"/>
  <rect x="232" y="213" width="5" height="23" rx="2" fill="#b0aea6" opacity="0.7"/>
  <rect x="245" y="212" width="5" height="24" rx="2" fill="#b0aea6" opacity="0.7"/>

  <!-- ═══════════ KRISHNA — charioteer ═══════════ -->
  <!-- Body / dhoti (yellow saffron) -->
  <ellipse cx="415" cy="185" rx="14" ry="20" fill="#c8860a" opacity="0.9"/>
  <!-- Uttariya (yellow cloth draped) -->
  <path d="M402 170 Q408 160 415 165 Q422 160 428 170 Q425 175 415 172 Q405 175 402 170Z" fill="#d4960a" opacity="0.85"/>
  <!-- Krishna head -->
  <circle cx="415" cy="158" r="11" fill="#2a1a05" opacity="0.9"/>
  <!-- Peacock feather crown -->
  <path d="M415 147 Q413 136 411 128 Q416 133 415 125 Q418 133 419 128 Q420 136 415 147Z" fill="#2a6b1a" opacity="0.9"/>
  <circle cx="415" cy="127" r="3" fill="#1a4a8a" opacity="0.8"/>
  <circle cx="415" cy="127" r="1.5" fill="#d4860a"/>
  <!-- Flute (horizontal) -->
  <line x1="403" y1="172" x2="428" y2="168" stroke="#8B5E0A" stroke-width="2" opacity="0.7"/>
  <!-- Reins in hand -->
  <path d="M408 178 Q300 200 245 203" stroke="#6b4a10" stroke-width="1.5" fill="none" opacity="0.6"/>
  <path d="M408 180 Q300 202 245 206" stroke="#6b4a10" stroke-width="1.5" fill="none" opacity="0.6"/>

  <!-- Divine aura / halo around Krishna -->
  <circle cx="415" cy="158" r="22" fill="none" stroke="#d4860a" stroke-width="1" opacity="0.4"/>
  <circle cx="415" cy="158" r="28" fill="none" stroke="#d4860a" stroke-width="0.5" opacity="0.2"/>

  <!-- ═══════════ ARJUNA — warrior ═══════════ -->
  <!-- Armour body (dark bronze) -->
  <ellipse cx="480" cy="182" rx="13" ry="20" fill="#4a3010" opacity="0.9"/>
  <!-- Chest armour plate -->
  <ellipse cx="480" cy="180" rx="10" ry="12" fill="#6b4a1a" opacity="0.8"/>
  <!-- Arjuna head -->
  <circle cx="480" cy="156" r="11" fill="#3d2208" opacity="0.9"/>
  <!-- Warrior crown / helmet -->
  <path d="M470 155 Q475 143 480 140 Q485 143 490 155Z" fill="#8B5E0A" opacity="0.9"/>
  <line x1="480" y1="140" x2="480" y2="133" stroke="#d4860a" stroke-width="1.5"/>
  <circle cx="480" cy="132" r="2.5" fill="#d4860a" opacity="0.9"/>
  <!-- Gandiva bow — raised -->
  <path d="M492 140 Q512 162 495 185" stroke="#8B5E0A" stroke-width="2.5" fill="none" filter="url(#glow)"/>
  <line x1="492" y1="140" x2="495" y2="185" stroke="#d4860a" stroke-width="0.8" opacity="0.7"/>
  <!-- Arrow nocked (pointing forward) -->
  <line x1="480" y1="168" x2="515" y2="158" stroke="#d4860a" stroke-width="1.2" opacity="0.8"/>
  <polygon points="515,158 510,154 511,162" fill="#d4860a" opacity="0.8"/>
  <!-- Quiver on back -->
  <rect x="464" y="160" width="8" height="22" rx="3" fill="#3d1a00" stroke="#6b4a1a" stroke-width="0.8"/>
  <!-- Arrow fletching in quiver -->
  <line x1="466" y1="160" x2="466" y2="153" stroke="#8B5E0A" stroke-width="1"/>
  <line x1="469" y1="160" x2="469" y2="151" stroke="#8B5E0A" stroke-width="1"/>
  <line x1="472" y1="160" x2="472" y2="153" stroke="#8B5E0A" stroke-width="1"/>

  <!-- ═══════════ TEXT ═══════════ -->
  <!-- Sanskrit verse — top centered, minimal -->
  <text x="450" y="35" text-anchor="middle" font-family="serif" font-size="12" fill="#d4860a" opacity="0.75" letter-spacing="3">कर्मण्येवाधिकारस्ते मा फलेषु कदाचन</text>

  <!-- Name — large, minimal -->
  <text x="450" y="120" text-anchor="middle" font-family="Georgia, serif" font-size="32" font-weight="700" fill="#e8d5a3" letter-spacing="6" filter="url(#softGlow)">SAKSHAM</text>

  <!-- Tagline -->
  <text x="450" y="142" text-anchor="middle" font-family="monospace" font-size="10" fill="#c8860a" letter-spacing="4" opacity="0.85">AnshXGrind  ·  Kurukshetra</text>

  <!-- Bottom line -->
  <line x1="150" y1="270" x2="750" y2="270" stroke="#b8730a" stroke-width="0.5" opacity="0.3"/>
  <text x="450" y="278" text-anchor="middle" font-family="monospace" font-size="8" fill="#8B5E0A" letter-spacing="2" opacity="0.6">Do your duty. Without desire for the fruit.</text>

</svg>

<br/>

[![Portfolio](https://img.shields.io/badge/portfolio-saksham--main.vercel.app-b8730a?style=flat-square&logo=vercel&logoColor=white)](http://saksham-main.vercel.app)&nbsp;
[![LinkedIn](https://img.shields.io/badge/linkedin-sakshamgrg-1a3a5c?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sakshamgrg)&nbsp;
[![GitHub](https://img.shields.io/badge/github-AnshXGrind-1a1a1a?style=flat-square&logo=github&logoColor=white)](https://github.com/AnshXGrind)

</div>

---

<div align="center">

```
  AI / ML Engineer  ·  Agent Builder  ·  Quant Systems  ·  C++ DSA  ·  Startup Founder
```

</div>

---

## `class Saksham`

```cpp
class Saksham : public Warrior {
private:
    string location  = "Kurukshetra, India";
    string creed     = "Do the work. Detach from the outcome.";

public:
    vector<string> arsenal = {
        "AI Agents & LLM Orchestration",
        "Algorithmic Trading & Quant Systems",
        "Data Structures & Algorithms — C++ is the weapon",
        "Building startups from zero"
    };

    string philosophy() const {
        return "कर्मण्येवाधिकारस्ते — Act. Build. Ship. No excuses.";
    }
};
```

---

## Stack

<div align="center">

**Languages**

![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

**AI / ML**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

**Quant / Trading**

![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)

**Tools**

![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)

</div>

---

## Projects

| Project | What it does | Stack |
|---|---|---|
| [lexiscan](https://github.com/AnshXGrind/lexiscan) | Lexical analysis & scanner engine | TypeScript |
| [medaiii](https://github.com/AnshXGrind/medaiii) | AI-powered medical intelligence | Python · AI/ML |
| [python-data-cleaning-project](https://github.com/AnshXGrind/python-data-cleaning-project) | Clean & prep raw datasets | Python · Jupyter |

---

## The Arjuna Mindset

```
Arjuna did not ask "will I win?"
He asked "what is my dharma?"

→ Ship the code. Not the hype.
→ Solve the problem. Not perform the solution.
→ Build the system. Then detach from the noise.

कर्म करो — फल की चिंता नहीं।
```

---

## Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=AnshXGrind&show_icons=true&theme=dark&hide_border=true&count_private=true&title_color=d4860a&icon_color=b8730a&text_color=e8d5a3&bg_color=0a0612" height="165"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=AnshXGrind&layout=compact&theme=dark&hide_border=true&langs_count=6&title_color=d4860a&text_color=e8d5a3&bg_color=0a0612" height="165"/>

<br/>

![GitHub Streak](https://streak-stats.demolab.com?user=AnshXGrind&theme=dark&hide_border=true&ring=d4860a&fire=b8730a&currStreakLabel=e8d5a3&background=0a0612&sideLabels=e8d5a3&dates=8B5E0A&currStreakNum=d4860a&sideNums=d4860a)

</div>

---

## Trophies

<div align="center">

![Trophies](https://github-profile-trophy.vercel.app/?username=AnshXGrind&theme=darkhub&no-frame=true&row=1&column=7&margin-w=6)

</div>

---

## The Path

```
                     ┌──────────────────────────────────────────┐
                     │          KURUKSHETRA ROADMAP              │
                     └──────────────────────────────────────────┘

  C++ & DSA          ──────────────────────►  Quant-Ready Algorithms
  AI Engineering     ──────────────────────►  Autonomous Agent Systems
  Algo Trading       ──────────────────────►  Systematic Quant Research
  Open Source        ──────────────────────►  Startup Founder

                                      "Nock the arrow. Release the outcome."
```

---

<div align="center">

![Visitor Count](https://komarev.com/ghpvc/?username=AnshXGrind&color=b8730a&style=flat-square&label=profile+views)

<br/><br/>

*"Arise, Arjuna. Your enemy is distraction. Your dharma is to build."*

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=2d1008&height=60&section=footer" width="100%"/>

</div>
