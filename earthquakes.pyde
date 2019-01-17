import csv

def setup():
    
    size(1000, 550)
    with open("allquakes20171010.csv") as f:
        reader = csv.reader(f)
        header = reader.next()

        global magnitudes
        magnitudes = []

        global locations
        locations = []
        
        global times
        times = []

        for field in reader:
            magnitude = float(field[4])
            magnitudes.append(magnitude)

            location = str(field[13])
            locations.append(location)
            
            time = splitTokens(field[0], "T .")
            times.append(time)

def draw():
    
    # visualization
    background(0)
    barScalar = 100
    barWidth = 2.99
    barTime = 4
    
    textPositionX = 3.33
    textPositionY = 400
    
    # interactivity
    mouseTrackerX = 1.5
    zeroCoordinateMagnitude = 0
    zeroCoordinateLocation = 0
    zeroCoordinateTime = 0
    
    # execution
    for magnitude in magnitudes:
        if mouseX < zeroCoordinateMagnitude - barWidth / mouseTrackerX or mouseX > zeroCoordinateMagnitude + barWidth / mouseTrackerX:
            fill(90)
        else:
            fill(60, 179, 113)
            textSize(12)
            textAlign(LEFT)
            text(magnitude, width / textPositionX, textPositionY + 45)
        ellipse(zeroCoordinateMagnitude, height / 2, barWidth, magnitude * barScalar)
        zeroCoordinateMagnitude = zeroCoordinateMagnitude + barTime

    for location in locations:
        if mouseX < zeroCoordinateLocation - barWidth / mouseTrackerX or mouseX > zeroCoordinateLocation + barWidth / mouseTrackerX:
            fill(0)
        else: 
            fill(60, 179, 113)
            textSize(12)
            textAlign(LEFT)
            text(location, width / textPositionX + 4, textPositionY + 65)
        zeroCoordinateLocation = zeroCoordinateLocation + barTime

    for time in times:
        if mouseX < zeroCoordinateTime - barWidth / mouseTrackerX or mouseX > zeroCoordinateTime + barWidth / mouseTrackerX:
            fill(0)
        else: 
            fill(60, 179, 113)
            textSize(12)
            textAlign(LEFT)
            text(time[1], width / textPositionX + 4, textPositionY + 85)
        zeroCoordinateTime = zeroCoordinateTime + barTime
          
    # static text
    fill(60, 179, 113)
    textSize(18)
    textAlign(LEFT)
    text("24 Hour Earthquake Activity: October 10th, 2017", 20, textPositionY - 360)

    fill(150)
    textSize(12)
    textAlign(RIGHT)
    text("Magnitude:", width / textPositionX, textPositionY + 45)
    
    fill(150)
    textSize(12)
    textAlign(RIGHT)
    text("Location:", width / textPositionX, textPositionY + 65)
    
    fill(150)
    textSize(12)
    textAlign(RIGHT)
    text("Time:", width / textPositionX, textPositionY + 85)
    
    fill(150)
    textSize(12)
    textAlign(RIGHT)
    text("Source:", width / textPositionX, textPositionY + 105)

    fill(60, 179, 113)
    textSize(12)
    textAlign(RIGHT)
    text("USGS 2017", 368, textPositionY + 105)
