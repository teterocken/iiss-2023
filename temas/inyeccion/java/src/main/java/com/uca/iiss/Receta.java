package com.uca.iiss;
import java.util.*;
public class Receta implements Iterable<Ingrediente>
{
	private Ingredientes ingredientes;
	public Receta(Ingrediente i1, Ingrediente i2, Ingrediente i3, Ingrediente i4)
	{
		ingredientes = new Ingredientes (4);
		boolean a = ingredientes.addIngrediente(i1);
		if(!a) {System.out.println("Ingrediente 1 no se ha podido añadir");}
		a = ingredientes.addIngrediente(i2);
		if(!a) {System.out.println("Ingrediente 2 no se ha podido añadir");}
		a = ingredientes.addIngrediente(i3);
		if(!a) {System.out.println("Ingrediente 3 no se ha podido añadir");}
		a = ingredientes.addIngrediente(i4);
		if(!a) {System.out.println("Ingrediente 4 no se ha podido añadir");}
	}
	public boolean addIngrediente (Ingrediente i)
	{
		return ingredientes.addIngrediente(i);
	}
	public boolean removeIngrediente (Ingrediente i)
	{
		return ingredientes.removeIngrediente(i);
	}
	public Iterator<Ingrediente> iterator()
	{
		return ingredientes.iterator();
	}
}
