# 🚀 TAAS-Bot — Thapar Amateur Astronomers Society Discord Bot

A custom **Discord Bot** built with `discord.py` and `Flask` for the **Thapar Amateur Astronomers Society (TAAS)** Discord server. The bot provides astronomy integrations (including NASA's Astronomy Picture of the Day API), server moderation/rules embeds, role information, and social media directory links.

---

## 📂 Repository Structure

```text
TAAS-Bot/
├── main.py            # Discord bot event handlers, commands, and NASA APOD integration
├── keep_alive.py      # Lightweight Flask web server on port 8080 for uptime monitoring
├── requirements.txt   # Python package dependencies
└── README.md          # Project documentation
```

---

## ✨ Supported Commands

| Command | Description |
| :--- | :--- |
| `/hello` | Greets the user and verifies bot responsiveness. |
| `/taas-links` | Sends a rich Discord embed containing official TAAS links (Instagram, WhatsApp community, and official Thapar website). |
| `/rules` | Displays the server code of conduct and moderation rules in a formatted embed. |
| `/roles` | Explains the server hierarchy and member role structure. |
| `/apod` | Fetches and displays **NASA's Astronomy Picture of the Day (APOD)** along with its title and scientific explanation. |
| `/random-image` / `/image` / `/picture` | Shares curated astronomy and society imagery in the channel. |

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sparsh0106/TAAS-Bot.git
   cd TAAS-Bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory containing your Discord Bot Token (and NASA API key if applicable):
   ```env
   TOKEN=your_discord_bot_token_here
   ```

4. **Run the bot**:
   ```bash
   python main.py
   ```

---

## 👤 Author

**Sparsh Agarwal** — [GitHub](https://github.com/sparsh0106) · [LinkedIn](https://www.linkedin.com/in/sparsh-agarwal-4b443b304/)
