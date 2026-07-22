# 외출 감지 기능 추가본

이 압축 파일은 기존 복약 감지 코드를 수정하거나 대체하지 않습니다.
기존 저장소 루트에 아래 파일과 폴더만 추가하세요.

- `run_exit.py`
- `exit_config.yaml`
- `exit_requirements.txt`
- `exit_system/`

기존 파일 중 아래 항목은 그대로 유지합니다.

- `main.py`
- `requirements.txt`
- `vision/`
- `utils/`
- `t.py`
- `outgoing_test`

## 설치

기존 가상환경에서 외출 감지용 의존성만 추가합니다.

```bash
pip install -r exit_requirements.txt
```

Picamera2는 Raspberry Pi OS에서 별도로 설치합니다.

```bash
sudo apt install python3-picamera2
```

## 실행

기존 복약 감지:

```bash
python main.py
```

외출 감지:

```bash
python run_exit.py
```

카메라 번호와 ROI/기준선은 `exit_config.yaml`에서만 조정합니다.
