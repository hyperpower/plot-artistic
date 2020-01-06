# libraries
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["savefig.format"] = 'png'


def get_color(index, groups):
    ng   = len(groups)

CC = plt.rcParams['axes.prop_cycle'].by_key()['color']

def get_pos(names, index, groups, td=0.9):
    ng   = len(groups)
    # td   = 0.9            # total width
    d    = td / ng          # delta width
    hd   = d * 0.5          # half delta width
    posc = np.arange(len(names))
    pos  = []
    for i in range(0, len(posc)):
        c  = posc[i]
        st = c - td * 0.5
        v  = st + (index + 0.5) * d
        pos.append(v)

    return pos

def add_value(ax, names, groups):
    for i in range(0, len(groups)):
        group = groups[i]
        pos   = get_pos(names, i, groups)
        ax.barh(pos, group["v"], 
                align ='center',
                height=0.9 / len(groups), 
                color = CC[i])

def add_delta_value(ax, names, groups):
    for i in range(0, len(groups)):
        group = groups[i]
        pos   = get_pos(names, i, groups)
        df    = []
        for v, dv in zip(group["v"], group["dv"]):
            df.append(v + dv)
        ax.barh(pos, df, 
                align ='center',
                height=0.9 / len(groups),
                color = CC[i],
                alpha = 0.5)

def add_value_text(ax, names, groups):
    for i in range(0, len(groups)):
        group = groups[i]
        pos   = get_pos(names, i, groups)
        dv    = min(group["v"]) * 0.05
        for p, v in zip(pos, group["v"]): 
            strv = "%.1f" % v
            ax.text(v-dv, p, strv, 
                    va    ="center",
                    ha    ="right",
                    color = "w",
                    fontweight='bold',
                    fontsize =12)

def add_final_value_text(ax, names, groups):
    for i in range(0, len(groups)):
        group = groups[i]
        pos   = get_pos(names, i, groups)
        sv    = min(group["v"]) * 0.05
        fv    = []
        for v, dv in zip(group["v"], group["dv"]):
            fv.append(v + dv)
        for p, v in zip(pos, fv): 
            strv = "%.1f" % v
            ax.text(v+sv, p, strv, 
                    va    = "center",
                    ha    = "left",
                    color = "k",
                    fontweight='bold',
                    fontsize =12)

def add_limit_line(ax, names, limitv):
    # print(len(names))
    ylim = ax.get_ylim()
    ax.plot([limitv, limitv],ylim, 
            "--", 
            color = "r",
            linewidth = 2.5)

def add_limit_text(ax, names, limitv):
    # print(len(names))
    props = dict(facecolor='w', alpha=1, ec = "r")
    textstr = "%.1f" % limitv
    # place a text box in upper left in axes coords
    ax.text(limitv, -0.7, textstr, 
            fontsize=14,
            va = 'center',
            ha = "center",
            bbox=props)

def plot(names, groups):
    fig, ax = plt.subplots()
    
    ax.set_ylim([-1, len(names) - 0.5])

    add_delta_value(ax, names, groups)
    add_value(ax, names, groups)
    add_value_text(ax, names, groups)
    add_final_value_text(ax, names, groups)
    add_limit_line(ax, names, 100)
    add_limit_text(ax, names, 100)

    ax.set_yticks(np.arange(len(names)))
    ax.set_yticklabels(names)
    # ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    # ax.set_title('How fast do you want to go today?')

    plt.savefig("fig", dpi = 300)

    # plt.show()


if __name__ == "__main__":
    names = ('Ground', '15kft', '25kft', '35kft', '15kft')
    g1    = {
        "name"   : "121011",
        "v"      : [98, 93, 34 ,56, 78],
        "dv"     : [4,  6 , 10, 23, 45]
    } 
    g2    = {
        "name"   : "161044",
        "v"      : [45, 53, 44 ,66, 48],
        "dv"     : [9,  17, 14, 13, 35]
    } 
    g3    = {
        "name"   : "391044",
        "v"      : [42, 56, 74 ,46, 58],
        "dv"     : [12,  7, 16, 2, 25]
    } 
    groups = [g1, g2, g3]
    plot(names, groups)