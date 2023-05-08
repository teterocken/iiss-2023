package com.uca.iiss;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
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