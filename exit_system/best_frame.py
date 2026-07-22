from __future__ import annotations

import json
import requests


class KakaoNotifier:
    def __init__(self, cfg: dict) -> None:
        self.enabled = bool(cfg["enabled"])
        self.access_token = str(cfg["access_token"])
        self.endpoint = str(cfg["endpoint"])
        self.link_url = str(cfg["link_url"])

    def send_to_me(self, text: str) -> bool:
        if not self.enabled:
            print("[KAKAO DISABLED]\n" + text)
            return True

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        template = {
            "object_type": "text",
            "text": text,
            "link": {
                "web_url": self.link_url,
                "mobile_web_url": self.link_url,
            },
            "button_title": "확인",
        }

        response = requests.post(
            self.endpoint,
            headers=headers,
            data={"template_object": json.dumps(template, ensure_ascii=False)},
            timeout=10,
        )
        if response.status_code != 200:
            print(f"[KAKAO ERROR] {response.status_code}: {response.text}")
            return False
        return True
