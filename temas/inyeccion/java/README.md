# Ejecución del programa

Situandose en la misma carpeta que el pom.xml y la carpeta src, ejecutar la siguiente orden: _mvn compile exec:java -Dexec.mainClass="com.uca.iiss.PruebaReceta"_

# Explicación del código

He creado una clase base llamada Ingrediente:

```python
public abstract class Ingrediente
{
	protected String nombre;
	public abstract void cocinar();
}
```

Tras esto, he creado 3 clases más que son subclases de Ingrediente:

```python
public class Carne extends Ingrediente
{
	public Carne(String nombre) {this.nombre=nombre;}
	public void cocinar(){System.out.println("Cocinamos muy bien el/la"+nombre);}
}
```

```python
public class Especia extends Ingrediente
{
	public Especia(String nombre) {this.nombre=nombre;}
	public void cocinar(){System.out.println("Agregamos una pizca de "+nombre);}
}
```

```python
public class Hortaliza extends Ingrediente
{
	public Hortaliza(String nombre) {this.nombre=nombre;}
	public void cocinar(){System.out.println("Cortamos y echamos el/la "+nombre);}
}
```

Tras esto, creo una clase llamada Ingredientes, que permite crear una lista iterable de ingredientes:

```python
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
```

Con esto, creé también una clase llamada Receta, que implementa una receta de 4 ingredientes, que permite también eliminar y añadir ingredientes, pero solo de un máximo de 4 ingredientes:

```python
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
```

Utilicé Spring para la inyección de dependencias, con el método de usar beans. Con las beans, cree una receta llamada polloplancha, que necesitaba de pollo, cebolla, sal y cebollino:

```xml
<beans>
	<bean id="pollo" class="com.uca.iiss.Carne">
		<constructor-arg index="0" value ="pollo"/>
	</bean>
	<bean id="cebolla" class="com.uca.iiss.Hortaliza">
		<constructor-arg index="0" value ="cebolla"/>
	</bean>
	<bean id="sal" class="com.uca.iiss.Especia">
		<constructor-arg index="0" value ="sal"/>
	</bean>
	<bean id="cebollino" class="com.uca.iiss.Hortaliza">
		<constructor-arg index="0" value ="cebollino"/>
	</bean>
	<bean id="polloplancha" class="com.uca.iiss.Receta">
		<constructor-arg index="0" ref="pollo"/>
        	<constructor-arg index="1" ref="cebolla"/>
        	<constructor-arg index="2" ref="sal"/>
        	<constructor-arg index="3" ref="cebollino"/>
	</bean>
</beans>
```

Tras esto, cree el siguiente código para efectuar la inyección de dependencias mediante beans y para cocinar cada ingrediente de la receta:

```python
public class PruebaReceta
{
	private static ApplicationContext context;

	public static void main (String[] args) throws Exception
	{
		context = new ClassPathXmlApplicationContext(new String[]{"receta.xml"});
		BeanFactory factory = context;
		Receta receta = (Receta) factory.getBean("polloplancha");
		for (Ingrediente i: receta) i.cocinar();
	}
}
```

La salida es la siguiente:

```
Cocinamos muy bien el/lapollo
Cortamos y echamos el/la cebolla  
Agregamos una pizca de sal        
Cortamos y echamos el/la cebollino
```

# Conclusión

Con este código conseguimos generar dependencias por parte de Receta al resto de tipos de Ingredientes.

Si bien Spring es una herramienta muy útil, hay que cuidar hasta el más mínimo detalle para que la inyección de dependencias funcione, cosa que, una vez se tiene más experiencia con la herramienta no será difícil, sin embargo, si es más complicado el realizar una primera toma de contacto.

Otro punto positivo de la herramienta es que permite realizar la inyección de dependencias sin necesidad de "ensuciar" demasiado el código, ya que todo se hace en un fichero xml a parte.
