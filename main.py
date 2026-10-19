from manim import *


class PuntoMuestraFinal(Scene):

    def obtener_rectangulos_riemann(
        self, axes, func, x_min, x_max, n, alpha, color, fill_opacity=0.55
    ):
        """Construye los rectángulos de la Suma de Riemann evaluando f(x_i^*)

        en x_i^* = x_{i-1} + alpha * dx, donde alpha in [0, 1].
        """
        dx = (x_max - x_min) / n
        rectangulos = VGroup()
        stroke_w = max(0.15, min(1.5, 8.0 / n))

        for i in range(n):
            x_left = x_min + i * dx
            x_right = x_left + dx
            x_star = x_left + alpha * dx
            y_height = func(x_star)

            rect = Polygon(
                axes.c2p(x_left, 0),
                axes.c2p(x_right, 0),
                axes.c2p(x_right, y_height),
                axes.c2p(x_left, y_height),
                fill_color=color,
                fill_opacity=fill_opacity,
                stroke_color=WHITE,
                stroke_width=stroke_w,
            )
            rectangulos.add(rect)
        return rectangulos

    def etiqueta_orador(self, texto):
        """Rótulo inferior izquierdo para identificar la voz activa (Criterio V6.c)."""
        badge = Tex(f"Voz: {texto}", color=GRAY_A).scale(0.52)
        badge.to_corner(DL, buff=0.2)
        return badge

    def construct(self):
        # =====================================================================
        # BLOQUE 1: CRISTIAN SÁEZ (0:00.0 - 1:14.2 | Duración exacta: 74.2 s)
        # =====================================================================
        orador_1 = self.etiqueta_orador("Cristian Sáez")

        # 1.1 Portada (0:00.0 - 0:13.5 | 13.5 s)
        titulo_proy = Tex(
            "\\textbf{Cálculo Intermedio MAT1188}\\\\",
            "Sumas de Riemann: Punto Medio y Punto Interior",
        ).scale(0.9)
        subtitulo_grupo = (
            Tex(
                "\\textbf{Grupo 11}\\\\",
                "Cristian Sáez $\\cdot$ Mathias Figueroa $\\cdot$ Catalina Durán $\\cdot$ Jaime Levil",
            )
            .scale(0.65)
            .next_to(titulo_proy, DOWN, buff=0.5)
            .set_color(BLUE_B)
        )

        self.play(
            FadeIn(orador_1),
            Write(titulo_proy),
            FadeIn(subtitulo_grupo),
            run_time=2.5,
        )
        self.wait(10.0)
        self.play(FadeOut(titulo_proy), FadeOut(subtitulo_grupo), run_time=1.0)

        # 1.2 Teoría Base, Símbolos y Condiciones (0:13.5 - 0:44.5 | 31.0 s)
        encabezado_b1 = (
            Tex("1. Fundamentos: Suma de Riemann en $[a, b]$")
            .scale(0.75)
            .to_corner(UL)
        )
        axes_intro = (
            Axes(
                x_range=[0, 5, 1],
                y_range=[0, 4, 1],
                x_length=5.5,
                y_length=3.2,
                axis_config={"color": WHITE},
            )
            .to_edge(LEFT, buff=0.6)
            .shift(DOWN * 0.25)
        )

        f_intro_fn = lambda x: 0.15 * (x - 1) * (x - 3) * (x - 4.5) + 1.8
        curva_intro = axes_intro.plot(f_intro_fn, x_range=[0.5, 4.5], color=BLUE)
        lbl_a = MathTex("a").scale(0.7).next_to(axes_intro.c2p(1, 0), DOWN)
        lbl_b = MathTex("b").scale(0.7).next_to(axes_intro.c2p(4, 0), DOWN)

        rects_intro = self.obtener_rectangulos_riemann(
            axes_intro, f_intro_fn, 1.0, 4.0, n=6, alpha=0.5, color=TEAL
        )

        panel_teoria = (
            VGroup(
                Tex(
                    "\\textbf{Condiciones para área geométrica:}", color=YELLOW
                ).scale(0.65),
                Tex(
                    "$\\bullet$ $f$ continua y $f(x) \\ge 0$ en $[a, b]$"
                ).scale(0.6),
                MathTex(
                    "S_n = \\sum_{i=1}^{n} f(x_i^*) \\Delta x", color=GREEN_B
                ).scale(0.8),
                Tex("$\\bullet$ $\\Delta x = \\frac{b-a}{n}$: ancho del subintervalo").scale(
                    0.58
                ),
                Tex(
                    "$\\bullet$ $x_i^* \\in [x_{i-1}, x_i]$: punto muestra"
                ).scale(0.58),
                Tex(
                    "$\\bullet$ $f(x_i^*)$: altura representativa"
                ).scale(0.58),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.22)
            .to_edge(RIGHT, buff=0.6)
            .shift(DOWN * 0.1)
        )

        self.play(
            Write(encabezado_b1),
            Create(axes_intro),
            Create(curva_intro),
            Write(lbl_a),
            Write(lbl_b),
            run_time=2.5,
        )
        self.play(Create(rects_intro), FadeIn(panel_teoria), run_time=2.5)
        self.wait(25.0)

        self.play(
            FadeOut(encabezado_b1),
            FadeOut(axes_intro),
            FadeOut(curva_intro),
            FadeOut(lbl_a),
            FadeOut(lbl_b),
            FadeOut(rects_intro),
            FadeOut(panel_teoria),
            run_time=1.0,
        )

        # 1.3 Pregunta Central (0:44.5 - 1:14.2 | 29.7 s)
        titulo_preg = (
            Tex("\\textbf{Pregunta Central}", color=YELLOW)
            .scale(0.9)
            .shift(UP * 1.2)
        )
        pregunta = Tex(
            "¿Por qué el punto muestra no tiene que ser necesariamente\\\\",
            "un extremo ni el punto medio?",
        ).scale(0.85)
        caja_preg = SurroundingRectangle(pregunta, color=YELLOW, buff=0.35)

        self.play(
            FadeIn(titulo_preg), Write(pregunta), Create(caja_preg), run_time=2.5
        )
        self.wait(26.2)
        self.play(
            FadeOut(titulo_preg),
            FadeOut(pregunta),
            FadeOut(caja_preg),
            FadeOut(orador_1),
            run_time=1.0,
        )

        # =====================================================================
        # BLOQUE 2: MATHIAS FIGUEROA (1:14.2 - 2:47.0 | Duración exacta: 92.8 s)
        # =====================================================================
        orador_2 = self.etiqueta_orador("Mathias Figueroa")
        titulo_b2 = (
            Tex("2. Elección del Punto Muestra $x_i^*$ en $[x_{i-1}, x_i]$")
            .scale(0.75)
            .to_corner(UL)
        )

        # 2.1 Planteamiento del Subintervalo (1:14.2 - 1:54.2 | 40.0 s)
        self.play(FadeIn(orador_2), Write(titulo_b2), run_time=1.5)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=6.6,
            y_length=3.5,
            axis_config={"color": WHITE},
        ).shift(UP * 0.35)

        f_b2 = lambda x: 0.5 * (x - 2) ** 2 + 1
        func = axes.plot(f_b2, x_range=[0, 5.3], color=BLUE)
        func_label = (
            MathTex("f(x) = \\frac{1}{2}(x-2)^2 + 1")
            .scale(0.65)
            .next_to(axes.c2p(4.8, f_b2(4.8)), LEFT, buff=0.4)
        )

        self.play(Create(axes), Create(func), Write(func_label), run_time=2.5)

        x_i_minus_1 = 2.0
        x_i = 4.0

        line_left = axes.get_vertical_line(
            axes.c2p(x_i_minus_1, f_b2(x_i_minus_1)), color=YELLOW
        )
        line_right = axes.get_vertical_line(
            axes.c2p(x_i, f_b2(x_i)), color=YELLOW
        )

        label_left = (
            MathTex("x_{i-1} = 2")
            .scale(0.62)
            .next_to(axes.c2p(x_i_minus_1, 0), DOWN, buff=0.15)
        )
        label_right = (
            MathTex("x_i = 4")
            .scale(0.62)
            .next_to(axes.c2p(x_i, 0), DOWN, buff=0.15)
        )

        brace = BraceBetweenPoints(
            axes.c2p(x_i_minus_1, -0.5), axes.c2p(x_i, -0.5), direction=DOWN
        )
        brace_label = (
            MathTex("\\Delta x = 2")
            .scale(0.7)
            .next_to(brace, DOWN, buff=0.1)
        )

        self.play(
            Create(line_left),
            Create(line_right),
            Write(label_left),
            Write(label_right),
            Create(brace),
            Write(brace_label),
            run_time=2.5,
        )
        self.wait(33.5)

        # 2.2 Recorrido Dinámico de x_i^* (1:54.2 - 2:30.0 | 35.8 s)
        x_star = ValueTracker(2.0)

        rect = always_redraw(
            lambda: Polygon(
                axes.c2p(x_i_minus_1, 0),
                axes.c2p(x_i, 0),
                axes.c2p(x_i, f_b2(x_star.get_value())),
                axes.c2p(x_i_minus_1, f_b2(x_star.get_value())),
                fill_opacity=0.5,
                fill_color=GREEN,
                stroke_color=GREEN,
            )
        )

        dot = always_redraw(
            lambda: Dot(
                axes.c2p(x_star.get_value(), f_b2(x_star.get_value())),
                color=RED,
            )
        )
        label_star = always_redraw(
            lambda: MathTex("f(x_i^*)")
            .scale(0.72)
            .next_to(dot, UP, buff=0.15)
        )

        panel_datos = always_redraw(
            lambda: VGroup(
                Tex("Punto $x_i^*$: "),
                DecimalNumber(
                    x_star.get_value(), num_decimal_places=2, color=RED
                ),
                Tex("   Altura $f(x_i^*)$: "),
                DecimalNumber(
                    f_b2(x_star.get_value()), num_decimal_places=2, color=GREEN
                ),
            )
            .arrange(RIGHT, buff=0.12)
            .scale(0.65)
            .to_corner(UR)
        )

        # 2.2a Extremo izquierdo estático hasta 2:06.0 (1:54.2 - 2:06.0 | 11.8 s)
        self.play(
            Create(rect),
            Create(dot),
            Write(label_star),
            Write(panel_datos),
            run_time=1.8,
        )
        self.wait(10.0)

        # 2.2b Se mueve en 2:06.0 al Extremo derecho y espera hasta 2:12.0 (6.0 s totales)
        self.play(x_star.animate.set_value(4.0), run_time=1.5)
        self.wait(4.5)

        # 2.2c Se mueve en 2:12.0 al Punto Medio y espera hasta 2:25.0 (13.0 s totales)
        self.play(x_star.animate.set_value(3.0), run_time=1.5)
        mid_label = Tex("Punto Medio").scale(0.62).next_to(dot, UP, buff=0.8)
        mid_arrow = Arrow(
            mid_label.get_bottom(), dot.get_top(), buff=0.1, color=YELLOW
        )
        self.play(FadeIn(mid_label), GrowArrow(mid_arrow), run_time=0.8)
        self.wait(10.0)
        self.play(FadeOut(mid_label), FadeOut(mid_arrow), run_time=0.7)

        # 2.2d Se mueve en 2:25.0 al Punto Interior y llega a 2:30.0 (5.0 s totales)
        self.play(x_star.animate.set_value(2.35), run_time=1.5)
        int_label = (
            Tex("Punto Interior ($x_i^* = 2.35$)", color=YELLOW)
            .scale(0.62)
            .next_to(dot, UP, buff=0.8)
        )
        int_arrow = Arrow(
            int_label.get_bottom(), dot.get_top(), buff=0.1, color=YELLOW
        )
        self.play(FadeIn(int_label), GrowArrow(int_arrow), run_time=0.7)
        self.wait(2.1)
        self.play(FadeOut(int_label), FadeOut(int_arrow), run_time=0.7)

        # 2.3 Conclusión Geométrica Local aparece en 2:30.0 (2:30.0 - 2:47.0 | 17.0 s)
        conclusion_text = Tex(
            "Cualquier punto $x_i^* \\in [x_{i-1}, x_i]$ determina una altura representativa válida $f(x_i^*)$.\\\\",
            "No es requisito usar los extremos ni el punto medio para construir la suma.",
        ).scale(0.58)
        conclusion_rect = SurroundingRectangle(
            conclusion_text,
            color=YELLOW,
            fill_color=BLACK,
            fill_opacity=0.95,
            buff=0.18,
        )
        grupo_conc_b2 = (
            VGroup(conclusion_rect, conclusion_text)
            .to_edge(DOWN, buff=0.15)
            .shift(RIGHT * 1.1)
        )

        self.play(
            FadeOut(brace),
            FadeOut(brace_label),
            FadeIn(grupo_conc_b2),
            run_time=1.5,
        )
        self.wait(14.5)

        self.play(
            FadeOut(titulo_b2),
            FadeOut(axes),
            FadeOut(func),
            FadeOut(func_label),
            FadeOut(line_left),
            FadeOut(line_right),
            FadeOut(label_left),
            FadeOut(label_right),
            FadeOut(rect),
            FadeOut(dot),
            FadeOut(label_star),
            FadeOut(panel_datos),
            FadeOut(grupo_conc_b2),
            FadeOut(orador_2),
            run_time=1.0,
        )

        # =====================================================================
        # BLOQUE 3: CATALINA DURÁN (2:47.0 - 4:30.0 | Duración exacta: 103.0 s)
        # =====================================================================
        orador_3 = self.etiqueta_orador("Catalina Durán")
        titulo_b3 = (
            Tex(
                "3. Ejemplo Propio: $f(x) = x^2$ en $[0, 2]$ con $n = 4$ ($\\Delta x = 0.5$)"
            )
            .scale(0.72)
            .to_corner(UL)
        )

        # 3.1 Planteamiento Pantalla Dividida (2:47.0 - 3:01.0 | 14.0 s)
        self.play(FadeIn(orador_3), Write(titulo_b3), run_time=1.5)

        axes_left = (
            Axes(
                x_range=[0, 2.3, 0.5],
                y_range=[0, 4.5, 1],
                x_length=4.9,
                y_length=2.9,
                axis_config={"color": WHITE},
            )
            .to_edge(LEFT, buff=0.7)
            .shift(UP * 0.55)
        )

        axes_right = (
            Axes(
                x_range=[0, 2.3, 0.5],
                y_range=[0, 4.5, 1],
                x_length=4.9,
                y_length=2.9,
                axis_config={"color": WHITE},
            )
            .to_edge(RIGHT, buff=0.7)
            .shift(UP * 0.55)
        )

        f_ej = lambda x: x**2
        curva_left = axes_left.plot(f_ej, x_range=[0, 2.05], color=BLUE)
        curva_right = axes_right.plot(f_ej, x_range=[0, 2.05], color=BLUE)

        sub_left = (
            Tex("Punto Medio ($50\\%$ del subintervalo)", color=TEAL_B)
            .scale(0.58)
            .next_to(axes_left, UP, buff=0.12)
        )
        sub_right = (
            Tex("Punto Interior ($80\\%$ del subintervalo)", color=ORANGE)
            .scale(0.58)
            .next_to(axes_right, UP, buff=0.12)
        )

        self.play(
            Create(axes_left),
            Create(curva_left),
            Write(sub_left),
            Create(axes_right),
            Create(curva_right),
            Write(sub_right),
            run_time=2.5,
        )
        self.wait(10.0)

        # 3.2a Caso 1: Punto Medio (3:01.0 - 3:22.0 | 21.0 s)
        rects_mid = self.obtener_rectangulos_riemann(
            axes_left, f_ej, 0.0, 2.0, n=4, alpha=0.5, color=TEAL
        )
        puntos_mid = VGroup(
            *[
                Dot(axes_left.c2p(x_s, f_ej(x_s)), color=YELLOW, radius=0.055)
                for x_s in [0.25, 0.75, 1.25, 1.75]
            ]
        )
        calc_mid = (
            MathTex(
                "x_i^* \\in \\{0.25, 0.75, 1.25, 1.75\\}\\\\",
                "S_4^{\\text{medio}} = \\sum_{i=1}^4 (x_i^*)^2 (0.5) = 2.625",
                color=TEAL_A,
            )
            .scale(0.55)
            .next_to(axes_left, DOWN, buff=0.15)
        )

        self.play(
            Create(rects_mid), FadeIn(puntos_mid), Write(calc_mid), run_time=2.5
        )
        self.wait(18.5)

        # 3.2b Caso 2: Punto Interior al 80% (3:22.0 - 3:48.0 | 26.0 s -> retrasa 3s el bloque siguiente)
        rects_int = self.obtener_rectangulos_riemann(
            axes_right, f_ej, 0.0, 2.0, n=4, alpha=0.8, color=ORANGE
        )
        puntos_int = VGroup(
            *[
                Dot(axes_right.c2p(x_s, f_ej(x_s)), color=RED, radius=0.055)
                for x_s in [0.4, 0.9, 1.4, 1.9]
            ]
        )
        calc_int = (
            MathTex(
                "x_i^* \\in \\{0.40, 0.90, 1.40, 1.90\\}\\\\",
                "S_4^{\\text{interior}} = \\sum_{i=1}^4 (x_i^*)^2 (0.5) = 3.270",
                color=GOLD_A,
            )
            .scale(0.55)
            .next_to(axes_right, DOWN, buff=0.15)
        )

        self.play(
            Create(rects_int), FadeIn(puntos_int), Write(calc_int), run_time=2.5
        )
        self.wait(23.5)

        # 3.3 Comparación con Valor Exacto aparece en 3:48.0-3:49.0 (3:48.0 - 4:30.0 | 42.0 s)
        texto_comp = (
            VGroup(
                Tex(
                    "\\textbf{Valor exacto:} $\\int_0^2 x^2\\,dx = \\frac{8}{3} \\approx 2.667$ \\quad $|$ \\quad "
                    "\\textbf{Punto Medio:} $2.625$ (error $1.6\\%$) \\quad $|$ \\quad "
                    "\\textbf{Punto Interior:} $3.270$ (error $22.6\\%$)"
                ).scale(0.50),
                Tex(
                    "Para $n$ finito, cambiar $x_i^*$ modifica las alturas $f(x_i^*)$, pero ambas son Sumas de Riemann legítimas."
                ).scale(0.50),
            )
            .arrange(DOWN, buff=0.14)
        )
        panel_comp = SurroundingRectangle(
            texto_comp,
            color=BLUE_B,
            fill_color=BLACK,
            fill_opacity=0.95,
            buff=0.16,
        )
        grupo_comp_b3 = VGroup(panel_comp, texto_comp).to_edge(DOWN, buff=0.55)

        self.play(
            FadeOut(calc_mid),
            FadeOut(calc_int),
            FadeIn(grupo_comp_b3),
            run_time=1.5,
        )
        self.wait(39.5)

        self.play(
            FadeOut(grupo_comp_b3),
            FadeOut(puntos_mid),
            FadeOut(puntos_int),
            FadeOut(orador_3),
            run_time=1.0,
        )

        # =====================================================================
        # BLOQUE 4: JAIME LEVIL (4:30.0 - 5:39.0 | Duración exacta: 69.0 s)
        # =====================================================================
        orador_4 = self.etiqueta_orador("Jaime Levil")
        titulo_b4 = (
            Tex(
                "4. Paso al Límite: Refinamiento $n \\to \\infty$ ($\\Delta x \\to 0$)"
            )
            .scale(0.75)
            .to_corner(UL)
        )

        # 4.1a Estado inicial n = 4 hasta 4:43.0 (4:30.0 - 4:43.0 | 13.0 s)
        self.play(
            FadeIn(orador_4), Transform(titulo_b3, titulo_b4), run_time=1.5
        )

        lbl_s_mid = (
            Tex("$n = 4 \\implies S_n = 2.625$", color=TEAL_A)
            .scale(0.62)
            .next_to(axes_left, DOWN, buff=0.18)
        )
        lbl_s_int = (
            Tex("$n = 4 \\implies S_n = 3.270$", color=GOLD_A)
            .scale(0.62)
            .next_to(axes_right, DOWN, buff=0.18)
        )
        self.play(FadeIn(lbl_s_mid), FadeIn(lbl_s_int), run_time=1.0)
        self.wait(10.5)

        # 4.1b Primera animación en 4:43.0 -> n = 16 (4:43.0 - 4:50.0 | 7.0 s)
        rects_mid_16 = self.obtener_rectangulos_riemann(
            axes_left, f_ej, 0.0, 2.0, n=16, alpha=0.5, color=TEAL
        )
        rects_int_16 = self.obtener_rectangulos_riemann(
            axes_right, f_ej, 0.0, 2.0, n=16, alpha=0.8, color=ORANGE
        )
        lbl_mid_16 = (
            Tex("$n = 16 \\implies S_{16} = 2.664$", color=TEAL_A)
            .scale(0.62)
            .next_to(axes_left, DOWN, buff=0.18)
        )
        lbl_int_16 = (
            Tex("$n = 16 \\implies S_{16} = 2.818$", color=GOLD_A)
            .scale(0.62)
            .next_to(axes_right, DOWN, buff=0.18)
        )

        self.play(
            Transform(rects_mid, rects_mid_16),
            Transform(rects_int, rects_int_16),
            Transform(lbl_s_mid, lbl_mid_16),
            Transform(lbl_s_int, lbl_int_16),
            run_time=2.0,
        )
        self.wait(5.0)

        # 4.1c Segunda animación en 4:50.0 -> n = 50 (4:50.0 - 4:56.0 | 6.0 s)
        rects_mid_50 = self.obtener_rectangulos_riemann(
            axes_left, f_ej, 0.0, 2.0, n=50, alpha=0.5, color=TEAL
        )
        rects_int_50 = self.obtener_rectangulos_riemann(
            axes_right, f_ej, 0.0, 2.0, n=50, alpha=0.8, color=ORANGE
        )
        lbl_mid_50 = (
            Tex("$n = 50 \\implies S_{50} = 2.666$", color=TEAL_A)
            .scale(0.62)
            .next_to(axes_left, DOWN, buff=0.18)
        )
        lbl_int_50 = (
            Tex("$n = 50 \\implies S_{50} = 2.715$", color=GOLD_A)
            .scale(0.62)
            .next_to(axes_right, DOWN, buff=0.18)
        )

        self.play(
            Transform(rects_mid, rects_mid_50),
            Transform(rects_int, rects_int_50),
            Transform(lbl_s_mid, lbl_mid_50),
            Transform(lbl_s_int, lbl_int_50),
            run_time=2.0,
        )
        self.wait(4.0)

        # 4.1d Tercera animación en 4:56.0 -> n = 100 (4:56.0 - 5:05.0 | 9.0 s)
        rects_mid_100 = self.obtener_rectangulos_riemann(
            axes_left, f_ej, 0.0, 2.0, n=100, alpha=0.5, color=TEAL
        )
        rects_int_100 = self.obtener_rectangulos_riemann(
            axes_right, f_ej, 0.0, 2.0, n=100, alpha=0.8, color=ORANGE
        )
        lbl_mid_100 = (
            Tex("$n = 100 \\implies S_{100} \\approx 2.667$", color=TEAL_A)
            .scale(0.62)
            .next_to(axes_left, DOWN, buff=0.18)
        )
        lbl_int_100 = (
            Tex("$n = 100 \\implies S_{100} \\approx 2.691$", color=GOLD_A)
            .scale(0.62)
            .next_to(axes_right, DOWN, buff=0.18)
        )

        self.play(
            Transform(rects_mid, rects_mid_100),
            Transform(rects_int, rects_int_100),
            Transform(lbl_s_mid, lbl_mid_100),
            Transform(lbl_s_int, lbl_int_100),
            run_time=2.0,
        )
        self.wait(7.0)

        # 4.2 Bloque de texto aparece en 5:05.0 y transición en 5:29.0 (5:05.0 - 5:29.0 | 24.0 s)
        texto_final = (
            VGroup(
                Tex(
                    "\\textbf{Conclusión:} Cuando $n \\to \\infty$ ($\\Delta x \\to 0$), el subintervalo $[x_{i-1}, x_i]$ colapsa a un punto."
                ).scale(0.52),
                Tex(
                    "Por continuidad, toda elección de $x_i^*$ converge a la misma \\textbf{Integral Definida}:"
                ).scale(0.52),
                MathTex(
                    "\\lim_{n\\to\\infty} \\sum_{i=1}^n f(x_i^*)\\Delta x = \\int_a^b f(x)\\,dx = \\frac{8}{3}",
                    color=YELLOW,
                ).scale(0.62),
            )
            .arrange(DOWN, buff=0.12)
        )
        caja_final = SurroundingRectangle(
            texto_final,
            color=YELLOW,
            fill_color=BLACK,
            fill_opacity=0.95,
            buff=0.16,
        )
        grupo_final_b4 = VGroup(caja_final, texto_final).to_edge(DOWN, buff=0.48)

        self.play(
            FadeOut(lbl_s_mid),
            FadeOut(lbl_s_int),
            FadeIn(grupo_final_b4),
            run_time=1.5,
        )
        self.wait(21.5)

        self.play(
            FadeOut(titulo_b3),
            FadeOut(axes_left),
            FadeOut(axes_right),
            FadeOut(curva_left),
            FadeOut(curva_right),
            FadeOut(sub_left),
            FadeOut(sub_right),
            FadeOut(rects_mid),
            FadeOut(rects_int),
            FadeOut(grupo_final_b4),
            FadeOut(orador_4),
            run_time=1.0,
        )

        # =====================================================================
        # 4.3 CRÉDITOS, FUENTES, KDENLIVE Y DECLARACIÓN DE IA (5:29.0 - 5:39.0 | 10.0 s)
        # =====================================================================
        creditos = VGroup(
            Tex(
                "\\textbf{Créditos, Referencias y Declaración de IA}",
                color=YELLOW,
            ).scale(0.78),
            Tex(
                "\\textbf{Fuentes Matemáticas:}\\\\",
                "1. Apunte del curso: \\textit{Introducción a la integral}, MAT1188 (2026).\\\\",
                "2. Stewart, J. (2012). \\textit{Cálculo de una variable: Trascendentes tempranas} (7.a ed.). Cengage Learning.\\\\",
                "3. Thomas, G. B., Weir, M. \\& Hass, J. (2010). \\textit{Cálculo: Una variable} (12.a ed.). Pearson.",
            ).scale(0.52),
            Tex(
                "\\textbf{Software de Animación y Edición de Video:}\\\\",
                "$\\bullet$ Manim Community Developers (2026). \\textit{Manim} (v0.22.0). https://docs.manim.community/\\\\",
                "$\\bullet$ KDE Community (2026). \\textit{Kdenlive – Video Editor}. https://kdenlive.org/",
            ).scale(0.52),
            Tex(
                "\\textbf{Declaración de Uso de IA:}\\\\",
                "Se utilizó Gemini como apoyo en la estructuración de escenas en Manim y revisión de formato.\\\\",
                "Todos los cálculos matemáticos, parámetros y afirmaciones fueron verificados analíticamente por el Grupo 11.",
            ).scale(0.52),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.30)

        self.play(FadeIn(creditos), run_time=1.5)
        self.wait(8.5)