def get_arcgis_satellite_url(lat: float, lon: float, delta: float = 0.004) -> str:
    """
    Generates a direct ArcGIS World Imagery export URL for high-resolution optical satellite view.
    """
    tight_bbox = f"{lon - delta},{lat - delta},{lon + delta},{lat + delta}"
    url = (
        f"https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export?"
        f"bbox={tight_bbox}&bboxSR=4326&imageSR=4326&size=600,400&format=png&f=image"
    )
    return url
