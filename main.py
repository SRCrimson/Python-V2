import gestorAplicacion.mecanicas.Narrador as narrador
import gestorAplicacion.pjs.Player as player



pj = player.Player()
combate = narrador.combate(pj, "goblin")
narrador.window.after(100, combate.setTurno())
narrador.window.mainloop()











