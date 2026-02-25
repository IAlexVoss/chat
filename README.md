# Flet Chat Messenger

A simple real‑time chat application built with Flet.
It allows multiple users to join a chat room, send messages, and see system notifications when someone joins. The app demonstrates a clean separation of concerns with a structured architecture using controllers, models, and views.

## Features

- **Real‑time messaging** – messages appear instantly for all connected users (powered by Flet’s built‑in ``pubsub``).
- **Join notifications** – when a user joins, a system message is broadcast.
- **Persistent username** – the entered name is saved in the browser’s local storage ( ``client_storage`` ) and restored on next launch.
- **Clean UI** – avatars with initials and consistent colors per user.
- **Modular architecture** – easy to extend with new features.

## Tech Stack

- Python 3.8+
- [Flet](https://flet.dev/) – a framework that lets you build real‑time web, desktop and mobile apps in Python.

## Project Structure

```text
src/
├── main.py                 # Application entry point
├── app.py                  # Main App class – orchestrates UI and controllers
├── controllers/
│   ├── __init__.py
│   └── chat_controller.py  # Business logic: joining, sending, receiving messages
├── controls/
│   ├── __init__.py
│   └── chat_message.py     # Custom UI component for a chat message (avatar + text)
├── components/
│   ├── __init__.py
│   └── chat_controls.py    # Regular UI objects for app
├── models/
│   ├── __init__.py
│   └── message.py          # Data class representing a chat message
├── views/
│   ├── __init__.py
│   └── chat_view.py        # Assembles the main chat interface
└── utils/                  # (reserved for future helper functions)
```

## Module Description

- ``main.py`` – initializes the Flet page and hands control over to the ``App`` class.
- ``app.py`` - creates all UI controls (text fields, dialog, list view) and wires them together with the controller. It also holds the ``client_storage`` logic for persistent usernames.
- ``chat_controller.py`` – contains the event handlers (``join_click``, ``send_click``) and the ``on_message`` callback that updates the chat list. It receives all needed dependencies (page, chat list, input field, dialog) via its constructor.
- ``chat_message.py`` - a reusable ``Row`` subclass that displays an avatar (with initials) and the message text. The avatar color is derived from the username.
- ``message.py`` - a simple dataclass that holds the user, text, and message type (used for both chat messages and system messages).
- ``chat_view.py`` - builds the complete chat interface by combining the chat list, input field and send button. It accepts the actual controls and the send callback as parameters.

# Installation & Running

1. Clone the repository
```bash
git clone https://github.com/yourusername/flet-chat-messenger.git
cd flet-chat-messenger
```
2. Install dependencies
It is recommended to use a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: venv\Scripts\activate
pip install flet
```
3. Run the app
```bash
flet run main.py
```
The application will open in a native window. For a web version you can also run:
```bash
flet run --web main.py 
```

## Usage

1. When the app starts, a Welcome dialog appears. Enter your name and click “Join chat”.
2. The main chat window opens. Type a message in the text field at the bottom and press Enter or click the Send button.
3. Your message appears in the chat list, along with a system message informing others that you joined.
4. All connected users see messages in real time (test by opening multiple browser tabs/windows).

```note
For true multi‑user experience, the app must be hosted on a server.
Flet’s pubsub uses a WebSocket connection that works across different clients when the app is served from a reachable address.
```

## Architecture Overview

The project follows a variation of the Model‑View‑Controller (MVC) pattern:

- **Model** (``models/message.py``) - defines the data structure.
- **View** (``views/chat_view.py``) - describes the UI layout. It does not contain any business logic.
- **Conreoller** (``controllers/chat_controller.py``) - handles user actions and updates the model and view accordingly.
- **Controls** (``controls/chat_message.py``) - self‑contained, reusable UI components.
- **App** (``app.py``) - acts as the composition root: it instantiates all controls and the controller, then builds the final interface.

This separation makes the codebase easy to test, maintain, and extend.

## Future Improvements

- Add multiple chat rooms.
- Implement private messaging.
- Store chat history in a database.
- Add user authentication.
- Deploy the app to a cloud service (e.g., [Fly.io](https://fly.io/) Railway).

## License

This project is open source and available under the [MIT License](LICENSE).

___

Happy chatting!