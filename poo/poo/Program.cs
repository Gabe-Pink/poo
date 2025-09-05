using System;

namespace Poo
{
    public class Pessoa
    {
        public string Nome { get; set; }
        public int Idade { get; set; }

        public Pessoa(string nome, int idade)
        {
            Nome = nome;
            Idade = idade;
        }

        public void Apresentar()
        {
            Console.WriteLine($"Olá, eu sou {Nome} e tenho {Idade} anos.");
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            Pessoa p1 = new Pessoa("João", 30);
            Pessoa p2 = new Pessoa("ana", 25);

            Console.WriteLine($"Nome: { p1.Nome} Idade: { p1.Idade}");
            Console.WriteLine($"Nome: { p2.Nome} Idade: { p2.Idade}");
            ;
        }
    }
}