def turnOnSmokeController():
    print("Smoke controller turned on!")

def turnOffSmokeController():
    print("Smoke controller turned off!")

def turnOnSprinkler():
    print("Sprinkler Turned On!")
    return True

def turnOffSprinkler():
    print("Sprinkler Turned Off!")


def moveDown(currentPosition):
    x, y = currentPosition
    if y > 0:
        return [x, y - 1]
    else:
        print("Can't Move Downward!")
        return None

def moveUp(currentPosition):
    x, y = currentPosition
    if y < 3:
        return [x, y + 1]
    else:
        print("Can't Move Upward!")
        return None

def moveRight(currentPosition):
    x, y = currentPosition
    if x < 3:
        return [x + 1, y]
    else:
        print("Can't go Right!")
        return None

def moveLeft(currentPosition):
    x, y = currentPosition
    if x > 0:
        return [x - 1, y]
    else:
        print("Can't move left!")
        return None

def getCurrentPosition(x=0, y=0):
    return [x, y]

def fireLocation():
    return [2, 1]

def getCurrentPercept(currentLocation):
    isFire = fireLocation()
    x, y = currentLocation
    if x == isFire[0] and y == isFire[1]:
        print("Fire!")
        turnOnSprinkler()
        turnOffSmokeController()
        turnOffSprinkler()
        print("Area is Safe!")
        return True
    print("No Fire Here!")
    return False

def tryForLocation(location):
    visited = [[False for _ in range(4)] for _ in range(4)]
    locations = [location]  
    visited[location[0]][location[1]] = True  

    while locations:
        current_position = locations.pop() 
        percept = getCurrentPercept(current_position)
        if percept:
            print("Fire Over!")
            return current_position

        for move in [moveRight, moveLeft, moveUp, moveDown]:
            new_position = move(current_position)
            if new_position is not None:  
                x, y = new_position
                if not visited[x][y]:  
                    visited[x][y] = True
                    locations.append(new_position)

    print("Fire not found!")
    return location  

def main():
    current = getCurrentPosition(0, 0)
    final_position = tryForLocation(current)
    print("Final Position:", final_position)

if __name__ == '__main__':
    main()