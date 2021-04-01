#property copyright "Thieu Mao"
#property link      "https://language123.net/"
#property version   "1.00"

int My_Socket_Handle = INVALID_HANDLE; 

int OnInit() {
   My_Socket_Handle = Socket_Connect();
   return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason) {
   Socket_Close(My_Socket_Handle); 
}

double ask = 0;

void OnTick() {
   string str_price_ask = DoubleToString(SymbolInfoDouble(_Symbol, SYMBOL_ASK));
   double currentAsk = DoubleToString(SymbolInfoDouble(_Symbol, SYMBOL_ASK));
   if (ask != currentAsk) {
      ask = currentAsk;
      Socket_Send(My_Socket_Handle, str_price_ask); 
   }
   //Socket_Send(My_Socket_Handle, str_price_ask); 
}


int Socket_Connect() {
   int h_socket = SocketCreate(SOCKET_DEFAULT);
   if(h_socket != INVALID_HANDLE) {
      if(SocketConnect(h_socket,"127.0.0.1",1307,2000)) {
         Print("Connected to Socket Server"); 
      }//if(SocketConnect
      else {
         Print("Fail connected to Socket Server. error code : ", GetLastError()); 
      }
   }//if(socket != INVALID_HANDLE)
   else {
      Print("Fail SocketCreate error code : ", GetLastError()); 
   }
   return h_socket; 
}

void Socket_Close(int socket_handle) {
   if(socket_handle != INVALID_HANDLE) {
      SocketClose(socket_handle);
      My_Socket_Handle = INVALID_HANDLE; 
      Print("Socket Closed");      
   }
}

int Socket_Send(int socket_handle,string str_data) {
   if(socket_handle == INVALID_HANDLE) return 0; 
   uchar bytes[]; 
   int byte_size = StringToCharArray(str_data,bytes)-1; 
   return SocketSend(socket_handle,bytes,byte_size);
}
