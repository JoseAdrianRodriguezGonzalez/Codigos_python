import instaloader
ig=instaloader.Instaloader(download_videos=False,download_video_thumbnails=False)
user=input("#Instagram account")
ig.download_profile(user,profile_pic_only=False)