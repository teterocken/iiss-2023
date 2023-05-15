package com.uca.iiss;
public class Especia extends Ingrediente
{
	public Especia(String nombre) {this.nombre=nombre;}
	public void cocinar(){System.out.println("Agregamos una pizca de "+nombre);}
}
