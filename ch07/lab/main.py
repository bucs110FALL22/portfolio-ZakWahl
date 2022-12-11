from rectangle import Rectangle
from surface import Surface

def test_rectangle():
    # Test the Rectangle class with the given values
    r = Rectangle(10, 10, 10, 10)
    assert (r.x, r.y, r.height, r.width) == (10,10,10,10)

    r = Rectangle(-1, 1, 1, 1)
    assert (r.x, r.y, r.height, r.width) == (0,1,1,1)

    r = Rectangle(1, -1, 1, 1)
    assert (r.x, r.y, r.height, r.width) == (1,0,1,1)

    r = Rectangle(1, 1, -1, 1)
    assert (r.x, r.y, r.height, r.width) == (1,1,0,1)

    r = Rectangle(1, 1, 1, -1)
    assert (r.x, r.y, r.height, r.width) == (1,1,1,0)


def test_surface():
    # Test the Surface class with the given values
    s = Surface("myimage.png", 10, 10, 10, 10)
    assert (s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10)

    srect = s.getRect()
    assert (srect.x,  s.getRect().y, srect.height,  srect.width) == (10,10,10,10)

    assert s.image

def main():
    test_rectangle()
    test_surface()
    print("Tests complete!")


if __name__ == "__main__":
    main()