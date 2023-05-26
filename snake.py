from turtle import Turtle

STEP = 20


class Snake:
    # Directions for Right, Up, Left, Down
    directions = [0, 90, 180, 270]

    def __init__(self):
        """ Initialize snake """
        self.seg_color = "white"
        self.shape = "square"
        self.segments: list[Turtle] = []
        self.add_tail(3)
        print('Snake Initialized')

    def add_head(self):
        """ Add new head in the moving direction """
        new_seg = Turtle(self.shape)
        new_seg.color(self.seg_color)
        new_seg.penup()

        loc = self.segments[0].position()
        new_seg.setpos(loc[0], loc[1])
        self.segments[0].fd(STEP)

        new_seg.setheading(self.segments[0].heading())
        self.segments.insert(1, new_seg)

    def add_tail(self, count=1):
        """ This method add tail
        Note: this method should be only used during initialization of snake"""
        for i in range(count):
            new_tail = Turtle(self.shape)
            new_tail.color(self.seg_color)
            new_tail.penup()

            if len(self.segments) > 0:
                new_tail.setpos(self.segments[-1].position()[0] - 20, self.segments[-1].position()[1])
                # print(self.segments[-1].position()[0])

            self.segments.append(new_tail)

    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(-90)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_right(self) -> None:
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def move(self) -> None:
        head = self.segments[0]
        heading = head.heading()
        head.fd(STEP)
        for i in range(1, len(self.segments)):
            seg = self.segments[i]
            seg.fd(STEP)
            old_head = seg.heading()
            self.segments[i].setheading(heading)
            heading = old_head

    def is_collided(self, size: tuple[int, int]) -> bool:
        seg_pos: set = set()
        for seg in self.segments:
            pos = seg.position()
            seg_pos.add(pos)
            if pos[0] >= size[0] / 2 - 10 \
                    or pos[0] <= -size[0] / 2 + 10 \
                    or pos[1] >= size[1] / 2 - 10 \
                    or pos[1] <= -size[1] / 2 + 10:
                return True

        if len(seg_pos) != len(self.segments):
            return True

        return False

    def head(self):
        return self.segments[0];
