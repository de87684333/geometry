def _validate_dimensions(width: float, height: float) -> None:
	"""Lève ValueError si width ou height est négatif."""
	if width < 0 or height < 0:
		raise ValueError("width and height must be non-negative")

def area(width: float, height: float) -> float:
	"""Retourne la surface d'un rectangle."""
	_validate_dimensions(width, height)
	return width * height

def perimeter(width: float, height: float) -> float:
	"""Retourne le périmètre d'un rectangle."""
	_validate_dimensions(width, height)
	return 2 * (width + height)
