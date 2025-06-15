from manim import *

class Thumbnail(Scene):
    def construct(self):

        t = ValueTracker(0.787)
        z = ValueTracker(3)
        e = ValueTracker(-1)
        d = ValueTracker(12)

        earth = ImageMobject("kepler/pics/earth.png")
        head = Tex("Keplersche Gesetze").scale(2).shift(UP*1.5)
        head2 = Tex("Keplersche Gesetze").scale(2.03).shift(UP*1.5).set_color(GRAY)

        earth.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (12*np.cos(4*t.get_value()) + d.get_value()))
        .set_y(z.get_value() * (12*np.sin(4*t.get_value()) + e.get_value()))
        )

        self.add(earth,head2,head)
        self.wait(frozen_frame=False)





class Opening(Scene):
    def construct(self):

        t = ValueTracker(0.787)
        z = ValueTracker(3)
        e = ValueTracker(-1)
        d = ValueTracker(12)

        sun = ImageMobject("kepler/pics/sun.jpg")
        mercury = ImageMobject("kepler/pics/mercury.png")
        venus = ImageMobject("kepler/pics/venus.jpg")
        earth = ImageMobject("kepler/pics/earth.png")
        mars = ImageMobject("kepler/pics/mars.jpg")
        jupiter = ImageMobject("kepler/pics/jupiter.jpg")
        saturn = ImageMobject("kepler/pics/saturn.jpg")
        uranus = ImageMobject("kepler/pics/uranus.jpg")
        neptune = ImageMobject("kepler/pics/neptune.jpg")
        blackhole = ImageMobject("kepler/pics/blackhole.png").scale(0.6).set_z_index(-1)

        head = Tex("Keplersche Gesetze").scale(2).shift(UP*1.5)
        head2 = Tex("Keplersche Gesetze").scale(2.03).shift(UP*1.5).set_color(GRAY)

        trace1 = TracedPath(mercury.get_center,stroke_color=GRAY_A,stroke_width=2, dissipating_time=0.7)
        trace2 = TracedPath(venus.get_center,stroke_color=GRAY_B,stroke_width=2, dissipating_time=1.2)
        trace3 = TracedPath(earth.get_center,stroke_color=GRAY_C,stroke_width=2, dissipating_time=3.1)
        trace4 = TracedPath(mars.get_center,stroke_color=GRAY_B,stroke_width=2, dissipating_time=3.4)
        trace5 = TracedPath(jupiter.get_center,stroke_color=GRAY_A,stroke_width=2, dissipating_time=5.5)
        trace6 = TracedPath(saturn.get_center,stroke_color=WHITE,stroke_width=2)
        trace7 = TracedPath(uranus.get_center,stroke_color=GRAY_A,stroke_width=2)
        trace8 = TracedPath(neptune.get_center,stroke_color=WHITE,stroke_width=2)

        traces = VGroup(trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8).set_z_index(-2)

        sun.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value()).set_x(z.get_value()*d.get_value()).set_y(z.get_value()*e.get_value()))

        mercury.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (4*np.cos(8*t.get_value()) + d.get_value() -1))
        .set_y(z.get_value() * (3.5*np.sin(8*t.get_value()) + e.get_value()))
        )

        venus.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (8*np.cos(6*t.get_value()) + d.get_value()))
        .set_y(z.get_value() * (8*np.sin(6*t.get_value()) + e.get_value()))
        )

        earth.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (12*np.cos(4*t.get_value()) + d.get_value()))
        .set_y(z.get_value() * (12*np.sin(4*t.get_value()) + e.get_value()))
        )

        mars.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (16*np.cos(2*t.get_value()) + d.get_value()))
        .set_y(z.get_value() * (16*np.sin(2*t.get_value()) + e.get_value()))
        )

        jupiter.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (20*np.cos(1*t.get_value()) + d.get_value()))
        .set_y(z.get_value() * (20*np.sin(1*t.get_value()) + e.get_value()))
        )

        saturn.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (24*np.cos(0.5*t.get_value()) + d.get_value()))
        .set_y(z.get_value() * (24*np.sin(0.5*t.get_value()) + e.get_value()))
        )

        uranus.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (28*np.cos(0.25*t.get_value() + PI/2) + d.get_value()))
        .set_y(z.get_value() * (28*np.sin(0.25*t.get_value() + PI/2) + e.get_value()))
        )

        neptune.add_updater(lambda mob: mob.scale_to_fit_height(2*z.get_value())
        .set_x(z.get_value() * (32*np.cos(0.125*t.get_value() - PI/5) + d.get_value()))
        .set_y(z.get_value() * (32*np.sin(0.125*t.get_value() - PI/5) + e.get_value()))
        )

        bodys = Group(sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune)

        self.add_sound("kepler/music/opening.wav")
        # self.add(NumberPlane())
        self.add(sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,head2,head)

        self.add(trace3)
        for mob in traces:
            mob.stroke_width = 0
        trace3.stroke_width = 3

        self.wait(frozen_frame=False)
        self.play(t.animate.set_value(0.927),z.animate.set_value(0.2),Unwrite(head2),Unwrite(head),
                  d.animate.set_value(5),
                  e.animate.set_value(11.727),
                  rate_func=rate_functions.ease_in_sine,run_time=6)
        self.play(d.animate.set_value(0), e.animate.set_value(0), t.animate.set_value(1.927), rate_func=linear, run_time=2)

        self.add(traces)
        for mob in traces:
            mob.stroke_width = 2

        # self.play(t.animate.set_value(8), rate_func=rate_functions.ease_out_sine, run_time=12.073)
        self.play(t.animate.set_value(5.8975), rate_func=rate_functions.ease_out_sine, run_time=8.9)
        self.remove(sun)
        self.add(blackhole)
        # self.play(t.animate.set_value(8), rate_func=rate_functions.ease_out_sine, run_time=2)
        
        self.play(z.animate.set_value(0.0001), rate_func=rate_functions.ease_in_sine, run_time=3)

        self.play(FadeOut(bodys,traces))
        self.wait()
        self.play(FadeOut(blackhole))
        self.wait()





class FirstLaw(Scene):
    def construct(self):

        head = Tex("Erstes Keplersches Gesetz (Ellipsensatz):").to_edge(UP).shift(DOWN*2)
        law1 = Tex("Die Bahn eines jeden Planeten ist eine ","Ellipse"," wobei die Sonne in einem der beiden ","Brennpunkte"," steht.").scale(0.8).shift(DOWN*0.5)
        law1[1].set_color(YELLOW)
        law1[3].set_color(YELLOW)

        self.wait()
        self.play(Write(head), run_time=3)
        self.wait()
        self.play(Write(law1[:2]), run_time=3)
        self.wait()
        self.play(Write(law1[2:]), run_time=3)
        self.wait()





class FirstLawExplanaition(Scene):
    def construct(self):


        a = ValueTracker(5)
        b = ValueTracker(5)
        t = ValueTracker(PI/2)

        elips = Ellipse(width=1, height=1, color = WHITE)
        f1 = Dot([0,0,0], color=GREEN).scale(1.8)
        f2 = Dot([0,0,0], color=GREEN).scale(1.8)
        p1 = Circle(radius=0.1, color=BLUE, fill_opacity=1).scale(1.5)

        l1 = Line(start=f1.get_center(), end=p1.get_center(), color = YELLOW)
        l2 = Line(start=f2.get_center(), end=p1.get_center(), color = YELLOW)

        l1tex = DecimalNumber(0,num_decimal_places=3)
        l2tex = DecimalNumber(0,num_decimal_places=3)
        sol1 = MathTex(r"=",r"10").to_edge(UR)
        sol1[1].set_color(YELLOW)
        sol2 = MathTex(r"+").next_to(sol1,LEFT*6)
        addend1 = DecimalNumber(0,num_decimal_places=3).next_to(sol1,LEFT*8)
        addend2 = DecimalNumber(0,num_decimal_places=3).next_to(sol1,LEFT*1)

        f1tex = Tex("Brennpunkt").set_color(YELLOW)
        f2tex = Tex("Brennpunkt").set_color(YELLOW)

        sun = ImageMobject("kepler/pics/sun.jpg").scale(0.3)
        earth = ImageMobject("kepler/pics/earth.png").scale(0.06)



        elips.add_updater(lambda mob: mob.become(Ellipse(width=a.get_value(), height=b.get_value(), color = WHITE)))
        f1.add_updater(lambda mob: mob.become(Dot([0.5 *np.sqrt(a.get_value()**2 - b.get_value()**2),0,0], color=GREEN).scale(1.8)))
        f2.add_updater(lambda mob: mob.become(Dot([-0.5 *np.sqrt(a.get_value()**2 - b.get_value()**2),0,0], color=GREEN).scale(1.8)))
        p1.add_updater(lambda mob: mob.set_x(0.5*a.get_value()*np.cos(t.get_value())).set_y(0.5*b.get_value()*np.sin(t.get_value())))

        l1.add_updater(lambda mob: mob.become(Line(start=f1.get_center(), end=p1.get_center(), color = YELLOW)))
        l2.add_updater(lambda mob: mob.become(Line(start=f2.get_center(), end=p1.get_center(), color = YELLOW)))

        l1tex.add_updater(lambda mob: mob.become(DecimalNumber(np.linalg.norm(p1.get_center()-f1.get_center()),num_decimal_places=3).rotate(l1.get_angle()-PI)).move_to(l1).shift(LEFT))
        l2tex.add_updater(lambda mob: mob.become(DecimalNumber(np.linalg.norm(p1.get_center()-f2.get_center()),num_decimal_places=3).rotate(l2.get_angle())).move_to(l2).shift(RIGHT))
        addend1.add_updater(lambda mob: mob.set_value(np.linalg.norm(p1.get_center()-f1.get_center())))
        addend2.add_updater(lambda mob: mob.set_value(np.linalg.norm(p1.get_center()-f2.get_center())))

        f1tex.add_updater(lambda mob: mob.next_to(f1,DL))
        f2tex.add_updater(lambda mob: mob.next_to(f2,DR))

        sun.add_updater(lambda mob: mob.move_to(f2))
        earth.add_updater(lambda mob:  mob.set_x(-1/0.2 * np.cos(2*PI*t.get_value())).set_y(-1/0.33 * np.sin(2*PI*t.get_value())))



        # self.add(NumberPlane())
        self.wait(1)
        self.play(Write(elips), Write(f1), Write(f2))
        self.wait(10)

        self.play(a.animate.set_value(10), run_time=6)

        self.play(Write(f2tex), Write(f1tex))
        self.wait(5)
        self.play(Unwrite(f2tex), Unwrite(f1tex))

        self.play(Write(p1))

        self.play(Write(l1), Write(l1tex), run_time =3)
        self.play(Write(l2), Write(l2tex), run_time =3)

        self.play(Write(sol1),Write(sol2),Write(addend1),Write(addend2))
        self.play(t.animate.set_value(5*PI/2), run_time=7)
        self.play(t.animate.set_value(2*PI),FadeIn(sun), run_time=2)

        self.play(b.animate.set_value(6.02),FadeOut(p1,l1,l2,l1tex,l2tex,addend1,addend2,sol1,sol2))

        t.set_value(0)
        self.play(FadeIn(earth))
        self.play(t.animate.set_value(1),
        rate_func=lambda x: 0.384141280489* x**4 +0.567515417564* x**3 -1.52391321184* x**2 +1.55437855424*x +0.0135589503036,
        run_time=6)
        self.play(t.animate.set_value(2),
        rate_func=lambda x: 0.384141280489* x**4 +0.567515417564* x**3 -1.52391321184* x**2 +1.55437855424*x +0.0135589503036,
        run_time=6)
        self.play(t.animate.set_value(3),
        rate_func=lambda x: 0.384141280489* x**4 +0.567515417564* x**3 -1.52391321184* x**2 +1.55437855424*x +0.0135589503036,
        run_time=6)





class SecondLaw(Scene):
    def construct(self):

        head = Tex("Zweites Keplersches Gesetz (Flächensatz):").to_edge(UP).shift(DOWN*2)
        law2 = Tex("Die Geschwindigkeit der Planeten auf ihrer ","Bahnellipse"," ist nicht konstant, sondern variiert so,"," dass ein von der Sonne zum Planeten gezogener Fahrstrahl in gleichen ","Zeiten"," gleich große ","Flächen"," überstreicht.").scale(0.8).shift(DOWN*0.5)

        law2[1].set_color(YELLOW)
        law2[4].set_color(YELLOW)
        law2[6].set_color(YELLOW)

        self.wait()
        self.play(Write(head), run_time=3)
        self.wait()
        self.play(Write(law2[:3]), run_time=6)
        self.wait()
        self.play(Write(law2[3:]), run_time=7)
        self.wait()





class SecondLawExplanaition(Scene):
    def construct(self):


        a = ValueTracker(10)
        b = ValueTracker(6.02)
        t = ValueTracker(0)


        elips = Ellipse(width=1, height=1, color = WHITE).set_z_index(-2)
        sun = ImageMobject("kepler/pics/sun.jpg").scale(0.3).shift(LEFT*4)
        earth = ImageMobject("kepler/pics/earth.png").scale(0.06).set_z_index(-1)
        f2 = Dot([0,0,0], color=GREEN).scale(1.8).set_opacity(0).set_z_index(-2)
        trace1 = TracedPath(earth.get_center, color=BLUE, fill_color=BLUE).set_opacity(0.5).set_z_index(-4)
        p1 = Polygon(sun.get_center(),[-3.3,-2.25,0],[0,-30,0],[4.86,-0.704,0], color=BLACK, fill_opacity=1).set_z_index(-3)
        p2 = Polygon(sun.get_center(),[-3.3,2.25,0],[0,30,0],[4.86,0.704,0], color=BLACK, fill_opacity=1).set_z_index(-3)
        t1 = MathTex(r" \Delta t",r"=1.3").shift(LEFT*6 +UP)
        t2 = MathTex(r" \Delta t",r"=1.3").shift(LEFT*-6 +UP)
        a1 = MathTex(r"A",r"=3.2").shift(LEFT*-4)
        a2 = MathTex(r"A",r"=3.2").shift(LEFT*3.5 +UP)
        t1[0].set_color(YELLOW)
        t2[0].set_color(YELLOW)
        a1[0].set_color(YELLOW)
        a2[0].set_color(YELLOW)

        elips.add_updater(lambda mob: mob.become(Ellipse(width=a.get_value(), height=b.get_value(), color = WHITE)))
        f2.add_updater(lambda mob: mob.become(Dot([-0.5 *np.sqrt(a.get_value()**2 - b.get_value()**2),0,0], color=GREEN).scale(1.8).set_opacity(0)))



        self.wait()
        self.add(p1,p2,trace1)
        earth.move_to([-4,0,0])

        self.wait(0.001, frozen_frame=False)

        self.add(sun,elips,f2,earth)
        self.play(FadeIn(earth), Write(elips), Write(f2),FadeIn(sun), run_time=3)
        earth.add_updater(lambda mob:  mob.set_x(-1/0.2 * np.cos(2*PI*t.get_value())).set_y(-1/0.33 * np.sin(2*PI*t.get_value())))

        self.play(t.animate.set_value(1),
        rate_func=lambda x: 0.384141280489* x**4 +0.567515417564* x**3 -1.52391321184* x**2 +1.55437855424*x +0.0135589503036,
        run_time=13)

        self.play(t.animate.set_value(2),
        rate_func=lambda x: 0.384141280489* x**4 +0.567515417564* x**3 -1.52391321184* x**2 +1.55437855424*x +0.0135589503036,
        run_time=13)

        self.play(Write(t1))
        self.wait(5)
        self.play(Write(a2))
        self.wait(5)
        self.play(Write(t2))
        self.wait(5)
        self.play(Write(a1))
        self.wait(1)





class ThirdLaw(Scene):
    def construct(self):

        head = Tex("Drittes Keplersches Gesetz:").to_edge(UP).shift(DOWN*2)
        law3 = Tex("Die ","Quadrate"," der ","Umlaufzeiten"," je zweier Planeten"," verhalten sich zueinander wie die ","Kuben"," (die dritten Potenzen) der ","großen Halbachsen"," ihrer Bahnellipsen.").scale(0.8).shift(DOWN*0.5)
        law3[1].set_color(YELLOW)
        law3[3].set_color(YELLOW)
        law3[6].set_color(YELLOW)
        law3[8].set_color(YELLOW)

        self.wait()
        self.play(Write(head), run_time=2.5)
        self.wait()
        self.play(Write(law3[:5]), run_time=3)
        self.wait()
        self.play(Write(law3[5:]), run_time=6)
        self.wait()





class ThirdLawExplanaition(Scene):
    def construct(self):


        formula1 = MathTex(r"T^{2}",r" \sim  ",r"a^{3} ").to_corner(UL)
        formula2 = MathTex(r"C=\frac{T^{2}}{a^{3}}").to_corner(UL).shift(DOWN*3)
        t2 = MathTex(r"T",r"=23.08").next_to(formula1,DOWN).to_edge(LEFT)
        t3 = MathTex(r"a",r"=14.1").next_to(t2,DOWN).to_edge(LEFT)
        rechnung1 = MathTex(r"C=\frac{23.08^{2}}{14.1^{3}}\approx 0.191").next_to(formula2,DOWN).to_edge(LEFT)

        t4 = MathTex(r"T",r"=37.1").next_to(formula1,DOWN).to_edge(LEFT)
        t5 = MathTex(r"a",r"=19.3").next_to(t4,DOWN).to_edge(LEFT)
        rechnung2 = MathTex(r"C=\frac{37.10^{2}}{19.3^{3}}\approx 0.191").next_to(t5,DOWN).to_edge(LEFT)

        rect1 = Rectangle(height=4, width=2.5).shift(4.75*RIGHT +UP*0.5).set_opacity(0)
        rect2 = Rectangle(height=0.4, width=2, color=BLACK, fill_opacity=1).shift(6*RIGHT +UP*1.1).set_opacity(1)

        c = MathTex(r"C=0.191")
        search = MathTex(r"T=?")
        search[0][0].set_color(BLUE)

        formula1[0][0].set_color(BLUE)
        formula1[2][0].set_color(GREEN)
        formula2[0][2].set_color(BLUE)
        formula2[0][5].set_color(GREEN)
        rechnung1[0][2:7].set_color(BLUE)
        rechnung1[0][9:13].set_color(GREEN)
        rechnung2[0][2:7].set_color(BLUE)
        rechnung2[0][9:13].set_color(GREEN)
        t2[0].set_color(BLUE)
        t3[0].set_color(GREEN)
        t4[0].set_color(BLUE)
        t5[0].set_color(GREEN)
        ha = Tex("große Halbachse").set_color(WHITE).shift(LEFT*2)
        l1 = Line(start=[0.8,2.05,0], end=[0.9,-2.6,0], color=YELLOW)

        img1 = ImageMobject("kepler/e0.5").scale(1.3).shift(RIGHT*2)
        img2 = ImageMobject("kepler/e0.8").scale(1.2).shift(RIGHT*3)
        img3 = ImageMobject("kepler/e0").scale(3).shift(RIGHT*2)

        self.add(img1)
        self.play(Write(formula1))
        self.wait(8)
        self.play(Write(l1), Write(ha))
        self.wait(11)
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(t3))
        self.wait(6)
        self.play(Circumscribe(rect1), run_time=2)
        self.wait(4)
        self.play(FadeOut(ha,l1))
        self.play(Write(formula2))
        self.wait(13)
        self.play(Write(rechnung1))
        self.wait(8)

        self.play(FadeIn(img2),FadeOut(img1,rechnung1,formula1,t2,t3),formula2.animate.to_corner(UL))
        self.wait(5)

        t4.next_to(formula2, DOWN).align_to(formula2,LEFT)
        t5.next_to(t4, DOWN).align_to(t4,LEFT)
        self.play(Write(t4),Write(t5))
        self.wait(5)

        rechnung2.next_to(t5, DOWN).align_to(t5,LEFT)
        self.play(Write(rechnung2))
        self.wait(6)

        self.play(FadeOut(t4,t5,rechnung2,img2))
        self.play(FadeIn(img3),FadeIn(rect2))
        self.wait(5)

        c.next_to(formula2, DOWN).align_to(formula2,LEFT)
        search.next_to(c, DOWN).align_to(c,LEFT)
        self.play(Write(c))
        self.play(Write(search))
        self.wait()