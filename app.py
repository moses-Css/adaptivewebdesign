from flask import Flask, render_template, request, make_response

app = Flask(__name__)

def detect_device(ua_string: str) -> str:
    """
    Heuristic user-agent detection:
    - tries to catch many tablet indicators first
    - then mobile indicators
    - special-case: android without 'mobile' => tablet
    - fallback => desktop
    This is intentionally conservative for demo purposes.
    """
    ua = (ua_string or "").lower()

    # common tablet indicators (order matters)
    tablet_keys = [
        "tablet", "ipad", "playbook", "silk", "kindle",
        "nexus 7", "nexus 9", "sm-t", "tab", "galaxy tab",
        "xoom", "transformer", "sch-i800"
    ]

    # common mobile indicators
    mobile_keys = [
        "mobile", "iphone", "ipod", "windows phone", "blackberry",
        "bb10", "opera mini", "phone", "android.*mobile"
    ]

    # check tablet keywords
    for k in tablet_keys:
        if k in ua:
            return "tablet"

    # check mobile keywords
    for k in mobile_keys:
        if k in ua:
            return "mobile"

    # special-case: android present but not mobile -> tablet
    if "android" in ua and "mobile" not in ua:
        return "tablet"

    # fallback
    return "desktop"


@app.route("/")
def index():
    # prefer cookie override (set by client-side script device-override.js)
    cookie_dev = request.cookies.get("detected_device")
    ua = request.headers.get("User-Agent", "")

    if cookie_dev in ("mobile", "tablet", "desktop"):
        device = cookie_dev
    else:
        device = detect_device(ua)

    # per-device content
    if device == "desktop":
        page_info = {
            "title": "AdaptiveSite — Ecommerce",
            "headline": "Sell anything. Fast.",
            "sub": "A modern ecommerce demo layout for desktop shoppers.",
            "bullets": ["Product grid", "Checkout flow", "Admin dashboard"],
        }
    elif device == "tablet":
        page_info = {
            "title": "AdaptiveSite — Studio",
            "headline": "Create. Showcase. Inspire.",
            "sub": "A clean studio portfolio layout tuned for tablets.",
            "bullets": ["Gallery", "Services", "Contact form"],
        }
    else:  # mobile
        page_info = {
            "title": "AdaptiveSite — Chatan App",
            "headline": "Chat with your people.",
            "sub": "Compact chat UI and quick actions, optimized for phones.",
            "bullets": ["Recent chats", "Quick replies", "Notifications"],
        }

    resp = make_response(render_template("index.html", device=device, ua=ua, page=page_info))
    return resp


@app.route("/clear-device-cookie")
def clear_device_cookie():
    """Utility route for development: clear the detected_device cookie and redirect to root."""
    resp = make_response(render_template("index.html", device="desktop", ua=request.headers.get("User-Agent", ""), page={
        "title": "AdaptiveSite — Demo",
        "headline": "Cleared device cookie",
        "sub": "Cookie removed; reload to let server detect UA again.",
        "bullets": []
    }))
    resp.set_cookie("detected_device", "", expires=0, path="/")
    return resp

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
