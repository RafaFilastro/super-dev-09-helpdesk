import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';

import { TicketService } from '../../../services/ticket.service';
import { TicketResposta, TicketAssociar } from '../../../models/tickets.model';

import { UsuarioResposta } from '../../../models/usuarios.model';
import { Modal } from '../../../shared/modal/modal';
import { UsuarioService } from '../../../services/usuario.service';

@Component({
  imports: [RouterLink, Modal, FormsModule],
  selector: 'app-listar',
  styleUrl: './listar.scss',
  templateUrl: './listar.html',
})
export class Listar {
  ticketService = inject(TicketService);
  usuarioService = inject(UsuarioService);

  tickets = signal<TicketResposta[]>([]);
  usuarios = signal<UsuarioResposta[]>([]);

  modalAssociarAberta = signal<boolean>(false);
  ticketSelecionado = signal<number | null>(null);

  ticketAssociar: TicketAssociar = {
    idUsuario: null,
  };

  ngOnInit() {
    this.carregarTickets();
    this.carregarUsuarios();
  }

  carregarUsuarios() {
    this.usuarioService.listar().subscribe({
      next: (usuarios) => this.usuarios.set(usuarios),
      error: (erro) => {
        console.error(erro);
        alert('Não foi possível listar os usuários');
      },
    });
  }

  carregarTickets() {
    this.ticketService.listar().subscribe({
      next: (tickets) => {
        this.tickets.set(tickets);
      },
      error: (erro) => {
        console.error(erro);
        alert('Não foi possível carregar os tickets');
      },
    });
  }

  abrirModalAssociar(ticketId: number){
    this.ticketSelecionado.set(ticketId);
    this.modalAssociarAberta.set(true);
  }

  associar() {
    this.ticketService.associar(this.ticketSelecionado()!, this.ticketAssociar).subscribe({
        next: () => {
            this.modalAssociarAberta.set(false);
            this.ticketAssociar = {
                idUsuario: null
            };

            alert("Ticket associado com sucesso");
            this.carregarTickets();
        },
        error: erro => {
            console.error(erro);
            alert("Não foi possível associar o ticket");
        }
    })
  }
}
