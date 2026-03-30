"""
generate_readme.py
==================
Generates a Kurukshetra-themed GitHub profile README.md

Usage:
    python generate_readme.py                  # writes README.md
    python generate_readme.py --preview        # prints to terminal
    python generate_readme.py -o my_readme.md  # custom output path

Customise the CONFIG dict at the top to make it your own.
"""

import argparse
import sys
from datetime import date

# ─────────────────────────────────────────────────────────────
#  CONFIG  ←  edit this section to personalise your README
# ─────────────────────────────────────────────────────────────
CONFIG = {
    "name":        "Saksham",
    "handle":      "AnshXGrind",
    "origin":      "Kurukshetra, Haryana",
    "base":        "Delhi, India",
    "tagline":     "From the land of the Gita · Building systems that matter",
    "mission":     "Build AI systems that change the game",
    "philosophy":  "Do the work. Trust the process. Ship.",

    "verse_hi":    "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।\nमा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥",
    "verse_en":    "You have a right to perform your prescribed duties,\nbut you are not entitled to the fruits of your actions.",
    "verse_src":   "Bhagavad Gita 2.47",

    "weapons": [
        ("C++",                "My Gandiva — low-latency, high-performance"),
        ("Python",             "ML, quant pipelines, automation"),
        ("TypeScript",         "Full-stack products & tooling"),
        ("AI / LLMs",          "RAG pipelines, agents, fine-tuning"),
        ("Algorithmic Trading","Markets as systems — find the edge"),
        ("DSA",                "The dharma of every engineer"),
    ],

    "pillars": [
        {
            "icon":  "⚔️",
            "title": "AI / ML Engineer",
            "desc":  "LLMs · RAG · autonomous agents that actually ship",
            "tags":  ["PyTorch", "LangChain", "OpenAI", "RAG"],
        },
        {
            "icon":  "◎",
            "title": "Quant / Algo Trader",
            "desc":  "Backtesting engines · signal generation · execution",
            "tags":  ["NumPy", "Pandas", "C++", "Backtesting"],
        },
        {
            "icon":  "▲",
            "title": "DSA in C++",
            "desc":  "Grinding NeetCode & Codeforces — graphs, DP, trees",
            "tags":  ["C++", "NeetCode", "Codeforces", "Graphs"],
        },
        {
            "icon":  "◈",
            "title": "Startup Founder",
            "desc":  "Building in public · ship fast · learn · iterate",
            "tags":  ["TypeScript", "Vercel", "Open Source"],
        },
    ],

    "projects": [
        {
            "name":  "lexiscan",
            "emoji": "⚡",
            "desc":  "Lexical analysis & scanner engine — parsing at the compiler level",
            "stack": ["TypeScript", "Compiler Design"],
            "url":   "https://github.com/AnshXGrind/lexiscan",
        },
        {
            "name":  "medaiii",
            "emoji": "🧬",
            "desc":  "AI-powered medical intelligence — LLMs applied to healthcare diagnostics",
            "stack": ["Python", "AI/ML", "LLM"],
            "url":   "https://github.com/AnshXGrind/medaiii",
        },
        {
            "name":  "python-data-cleaning-project",
            "emoji": "📊",
            "desc":  "End-to-end data cleaning & preprocessing pipeline for ML-ready datasets",
            "stack": ["Python", "Jupyter", "Pandas"],
            "url":   "https://github.com/AnshXGrind/python-data-cleaning-project",
        },
    ],

    "roadmap": [
        ("🟡", "AI/ML Engineer",   "→ Agent Systems Architect",
               "LLMs · RAG · multi-agent orchestration · autonomous systems"),
        ("🟣", "DSA in C++",       "→ Competitive + Quant Dev",
               "High-frequency logic · low-latency C++ · quant interview ready"),
        ("🟢", "Algo Trading",     "→ Systematic Quant Research",
               "Backtesting engines · signal generation · market microstructure"),
        ("🔴", "Builder",          "→ Startup Founder 🚀",
               "Ship something that matters · build in public"),
    ],

    "stats": {
        "repos": 19,
        "stars": 7,
    },

    "github_stats_theme": "radical",
    "github_stats_bg":    "04010a",
    "github_stats_title": "f5b300",
    "github_stats_text":  "c8a060",
    "github_stats_icon":  "7a5fd4",

    "contacts": {
        "GitHub": "https://github.com/AnshXGrind",
    },
}
# ─────────────────────────────────────────────────────────────


# ── helpers ───────────────────────────────────────────────────

def shields_badge(label: str, color: str, logo: str = "") -> str:
    """Return a shields.io badge markdown string."""
    label_enc = label.replace(" ", "_").replace("-", "--")
    logo_part = f"&logo={logo}" if logo else ""
    return (
        f"![{label}](https://img.shields.io/badge/{label_enc}-{color}"
        f"?style=flat-square{logo_part}&logoColor=white)"
    )


def tech_badge(name: str) -> str:
    """Map tech names to shields.io badge markdown."""
    palette = {
        "C++":          ("00599C", "cplusplus"),
        "Python":       ("3776AB", "python"),
        "TypeScript":   ("3178C6", "typescript"),
        "PyTorch":      ("EE4C2C", "pytorch"),
        "LangChain":    ("1C3C3C", "chainlink"),
        "OpenAI":       ("412991", "openai"),
        "RAG":          ("1D9E75", ""),
        "NumPy":        ("013243", "numpy"),
        "Pandas":       ("150458", "pandas"),
        "Backtesting":  ("f5b300", ""),
        "NeetCode":     ("FF2D55", ""),
        "Codeforces":   ("1F8ACB", ""),
        "Graphs":       ("7A5FD4", ""),
        "Vercel":       ("000000", "vercel"),
        "Open Source":  ("3DA639", "opensourceinitiative"),
        "Jupyter":      ("F37626", "jupyter"),
        "AI/ML":        ("FF6F00", ""),
        "LLM":          ("7F77DD", ""),
        "Compiler Design": ("5DA8D4", ""),
    }
    color, logo = palette.get(name, ("555555", ""))
    return shields_badge(name, color, logo)


def divider(style: str = "snake") -> str:
    """Return a decorative divider line."""
    dividers = {
        "snake":   "![snake](https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg)",
        "line":    "\n---\n",
        "ornament": "\n<div align='center'>⟨ ॐ ⟩</div>\n",
    }
    return dividers.get(style, "\n---\n")


# ── section builders ──────────────────────────────────────────

def section_banner(cfg: dict) -> str:
    handle = cfg["handle"]
    bg     = cfg["github_stats_bg"]
    return f"""\
<!--
  ██████╗ ██╗████████╗ █████╗     ███╗   ███╗ █████╗ ██████╗
  ██╔════╝ ██║╚══██╔══╝██╔══██╗    ████╗ ████║██╔══██╗██╔══██╗
  ██║  ███╗██║   ██║   ███████║    ██╔████╔██║███████║██████╔╝
  ██║   ██║██║   ██║   ██╔══██║    ██║╚██╔╝██║██╔══██║██╔═══╝
  ╚██████╔╝██║   ██║   ██║  ██║    ██║ ╚═╝ ██║██║  ██║██║
   ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝
-->

<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24&height=200&section=header&text=ॐ%20{handle}&fontSize=52&fontColor=f5c030&fontAlignY=38&desc={cfg["tagline"].replace(" ", "%20")}&descAlignY=58&descSize=14&descColor=c8900a)

</div>
"""


def section_verse(cfg: dict) -> str:
    lines_hi = cfg["verse_hi"].replace("\n", "  \n> ")
    lines_en = cfg["verse_en"].replace("\n", "  \n> *")
    src = cfg["verse_src"]
    return f"""\
<div align="center">

> **{lines_hi}**
>
> *{lines_en}*
>
> — {src}

*This is the code I ship by.*

</div>

"""


def section_about(cfg: dict) -> str:
    name    = cfg["name"]
    origin  = cfg["origin"]
    base    = cfg["base"]
    mission = cfg["mission"]
    philo   = cfg["philosophy"]

    weapons_lines = "\n".join(
        f'        "{w}",   // {desc}'
        for w, desc in cfg["weapons"]
    )

    return f"""\
## 🪖 About · परिचय

```cpp
// Like Arjuna on the battlefield — focused, skilled, relentless.

class {name} {{
  public:
    std::string origin   = "{origin}";
    std::string base     = "{base}";
    std::string mission  = "{mission}";

    std::vector<std::string> weapons = {{
{weapons_lines}
    }};

    auto philosophy() {{
        return "{philo}";
    }}
}};
```

"""


def section_pillars(cfg: dict) -> str:
    rows = ""
    for p in cfg["pillars"]:
        tag_str = " ".join(tech_badge(t) for t in p["tags"])
        rows += f"""\
### {p["icon"]} {p["title"]}
{p["desc"]}

{tag_str}

"""
    return f"## ⚙️ The Four Paths · चार मार्ग\n\n{rows}"


def section_projects(cfg: dict) -> str:
    cards = ""
    for proj in cfg["projects"]:
        stack_str = " · ".join(f"`{s}`" for s in proj["stack"])
        url       = proj["url"]
        cards += f"""\
#### {proj["emoji"]} [{proj["name"]}]({url})
{proj["desc"]}  
{stack_str}

"""
    return f"## ⚔️ Arsenal · शस्त्रागार\n\n{cards}*More being forged in the fire · stay tuned*\n\n"


def section_stats(cfg: dict) -> str:
    handle = cfg["handle"]
    bg     = cfg["github_stats_bg"]
    title  = cfg["github_stats_title"]
    text   = cfg["github_stats_text"]
    icon   = cfg["github_stats_icon"]
    theme  = cfg["github_stats_theme"]

    stats_url  = (f"https://github-readme-stats.vercel.app/api"
                  f"?username={handle}&show_icons=true&theme={theme}"
                  f"&hide_border=true&bg_color={bg}&title_color={title}"
                  f"&text_color={text}&icon_color={icon}")
    langs_url  = (f"https://github-readme-stats.vercel.app/api/top-langs/"
                  f"?username={handle}&layout=compact&theme={theme}"
                  f"&hide_border=true&bg_color={bg}&title_color={title}"
                  f"&text_color={text}&langs_count=8")
    streak_url = (f"https://streak-stats.demolab.com"
                  f"?user={handle}&theme=dark&hide_border=true"
                  f"&background={bg}&ring={title}&fire=c8900a&currStreakLabel=f5c840")

    repos = cfg["stats"]["repos"]
    stars = cfg["stats"]["stars"]

    return f"""\
## 📊 Battlefield Record · युद्ध सांख्यिकी

<div align="center">

| 🗂 Repos | ⭐ Stars | ∞ Grind |
|:-------:|:-------:|:-------:|
| **{repos}** | **{stars}** | **Always** |

<img src="{stats_url}" width="49%" />
<img src="{langs_url}" width="49%" />

<img src="{streak_url}" width="98%" />

</div>

"""


def section_roadmap(cfg: dict) -> str:
    items = ""
    for dot, from_, to_, detail in cfg["roadmap"]:
        items += f"- {dot} **{from_}** {to_}  \n  *{detail}*\n"
    return f"## 🗺 The Path · गीता मार्ग\n\n{items}\n"


def section_footer(cfg: dict) -> str:
    handle  = cfg["handle"]
    contact_badges = "  ".join(
        f"[![{name}]({shields_badge(name, '181717', name.lower())})]({url})"
        for name, url in cfg["contacts"].items()
    )
    year = date.today().year
    return f"""\

---

<div align="center">

ॐ &nbsp;·&nbsp; *{cfg["philosophy"]}*

{contact_badges}

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24&height=100&section=footer)

*© {year} {cfg["name"]} · Kurukshetra · Delhi · India*

</div>
"""


# ── assembler ─────────────────────────────────────────────────

SECTIONS = [
    section_banner,
    section_verse,
    section_about,
    section_pillars,
    section_projects,
    section_stats,
    section_roadmap,
    section_footer,
]


def build_readme(cfg: dict) -> str:
    """Assemble all sections into the final README string."""
    parts = [fn(cfg) for fn in SECTIONS]
    return "\n".join(parts)


# ── CLI ───────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a Kurukshetra-themed GitHub profile README.md"
    )
    parser.add_argument(
        "-o", "--output",
        default="README.md",
        help="Output file path (default: README.md)",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Print to stdout instead of writing a file",
    )
    return parser.parse_args()


def main():
    args   = parse_args()
    readme = build_readme(CONFIG)

    if args.preview:
        print(readme)
        return

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"✅  README written → {args.output}")
    print(f"    {len(readme):,} characters · {readme.count(chr(10))} lines")
    print(f"\n    Customise CONFIG at the top of this script, then re-run.")


if __name__ == "__main__":
    main()
