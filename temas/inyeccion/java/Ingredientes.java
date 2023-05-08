package com.uca.iiss;
import java.util.*;
public class Ingredientes implements Iterable<Ingrediente>
{
	private ArrayList<Ingrediente> ingredientes;
	public Ingredientes (int tam)
	{
		ingredientes = new ArrayList<Ingrediente>(tam);
	}
	public Iterator<Ingrediente> iterator()
	{
		return ingredientes.iterator();
	}
	public boolean addIngrediente (Ingrediente i)
	{
		return ingredientes.add(i);
	}
	public boolean removeIngrediente (Ingrediente i)
	{
		return ingredientes.remove(i);
	}
}