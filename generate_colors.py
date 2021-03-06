
def gen_colors(col):
    # generate colors
    complement = col.complementary_color()

    analogous = [col.analogous_color(0), col.analogous_color(1), col.analogous_color(-1)]

    # split_complement = [col, col.split_complementary_color(1), col.split_complementary_color(-1)]
    split_complement = []
    split_complement.append(col)
    split_complement.append(col.split_complementary_color(1))
    split_complement.append(col.split_complementary_color(-1))

    # triad = [col, col.triad_color(1), col.triad_color(-1)]
    triad = []
    triad.append(col)
    triad.append(col.triad_color(1))
    triad.append(col.triad_color(-1))

    # tetradic = [col.tetradic_color(0), col.tetradic_color(1), col.tetradic_color(3), col.tetradic_color(-2)]
    tetradic = []
    tetradic.append(col.tetradic_color(0))
    tetradic.append(col.tetradic_color(1))
    tetradic.append(col.tetradic_color(3))
    tetradic.append(col.tetradic_color(-2))

    colors = [col] + [complement] + analogous + split_complement + triad + tetradic
    return colors