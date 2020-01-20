# Import pygame into our programin
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 645
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    # Create a cube and place it in a scene, at position (0,0,0)
    # This cube has 1 unit of side, and is red
    obj1 = Object3d("TestObject")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, -1, 0)
    obj1.mesh = Mesh.create_cube((1, 1, 1))
    obj1.material = Material(color(1,0,0,1), "TestMaterial1")
    scene.add_object(obj1)

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, 0.75, 0)
    obj2.mesh = Mesh.create_cube((0.5, 0.5, 0.5))
    obj2.material = Material(color(0,1,0,1), "TestMaterial2")
    obj1.add_child(obj2)

    # Specify the rotation of the object. It will rotate 15 degrees around the axis given, 
    # every second
    angle = 0
    axis = vector3(1,0.7,0.2)
    axis.normalize()
    up, down, right, left,far, close,rot_up, rot_down, rot_right, rot_left, pag_down, pag_up = False, False, False, False, False, False,False,False,False,False,False,False

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    # Game loop, runs forever6
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return
                if (event.key == pygame.K_UP):
                    rot_up = True
                if (event.key == pygame.K_LEFT):
                    rot_left = True
                if (event.key == pygame.K_DOWN):
                    rot_down = True
                if (event.key == pygame.K_RIGHT):
                    rot_right = True
                if (event.key == pygame.K_PAGEDOWN):
                    pag_down = True
                if (event.key == pygame.K_PAGEUP):
                    pag_up = True
                if (event.key == pygame.K_w):
                   up = True
                if (event.key == pygame.K_d):
                    right = True
                if (event.key == pygame.K_s):
                    down = True
                if (event.key == pygame.K_a):
                    left = True
                if (event.key == pygame.K_q):
                    far = True
                if (event.key == pygame.K_e):
                    close = True

            elif (event.type == pygame.KEYUP):
                if (event.key == pygame.K_UP):
                    rot_up = False
                if (event.key == pygame.K_LEFT):
                    rot_left = False
                if (event.key == pygame.K_DOWN):
                    rot_down = False
                if (event.key == pygame.K_RIGHT):
                    rot_right = False
                if (event.key == pygame.K_PAGEDOWN):
                    pag_down = False
                if (event.key == pygame.K_PAGEUP):
                    pag_up = False
                if (event.key == pygame.K_w):
                   up = False
                if (event.key == pygame.K_d):
                    right = False
                if (event.key == pygame.K_s):
                    down = False
                if (event.key == pygame.K_a):
                    left = False
                if (event.key == pygame.K_q):
                    far = False
                if (event.key == pygame.K_e):
                    close = False

        if up:
            obj1.position += vector3(0, 0.002, 0)

        if right:
            obj1.position += vector3(0.002, 0, 0)

        if down:
            obj1.position += vector3(0, -0.002, 0)

        if left:
            obj1.position += vector3(-0.002, 0, 0)

        if far:
            obj1.position += vector3(0.002, 0, 0)

        if close:
            obj1.position += vector3(-0.002, 0, 0)

        if rot_up:
            q = from_rotation_vector((vector3(1,0,0) * math.radians(- 45) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation

        if rot_down:
            q = from_rotation_vector((vector3(1,0,0) * math.radians(45) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation

        if rot_right:
            q = from_rotation_vector((vector3(0,1,0) * math.radians(45) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation

        if rot_left:
            q = from_rotation_vector((vector3(0,1,0) * math.radians(- 45) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation

        if pag_down:
            q = from_rotation_vector((vector3(0,0,1) * math.radians(- 45) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation

        if pag_up:
            q = from_rotation_vector((vector3(0,0,1) * math.radians(45) * delta_time).to_np3())
            obj1.rotation = q * obj1.rotation




        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
