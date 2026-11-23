import cv2

info = cv2.getBuildInformation()

print(info)
for name in sorted(dir(cv2)):
    if name.startswith("COLOR_"):
        print(name, getattr(cv2, name))
