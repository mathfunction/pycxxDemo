#ifndef __PYCXX_BUFFER_HPP__
#define __PYCXX_BUFFER_HPP__
	
#include<iostream>
#include<sstream>
#include<vector>


//===========================================================
// global variables
namespace pycxx{

	class Pointer{
		private:
			const char* ptr;
			size_t n;
		public:
			void set(const char* bytes,size_t numBytes){
				this->ptr = bytes;
				this->n = numBytes;
			}
			const char* data(){
				return ptr;
			}

			const char operator[](int i){
				return ptr[i];
			}
			size_t size(){
				return n;
			}

			std::string makeStr(){
				return std::string(ptr,n);
			}
	};


	class Memory{
		private:
			std::vector<char> v_chars;   // in c++ \0  only use push_back , =
		public:

			std::string address(){
				std::ostringstream oss;
				oss << &v_chars;
				return oss.str();
			}

			void info(){
				std::cout << "+-----------------------------------+\n"; 
				std::cout << "Memory::info()\n\n";
				std::cout << "\t&address : " << this->address() <<  "\n";
				std::cout << "\t#bytes : " << v_chars.size() << "\n";
				std::cout << "+-----------------------------------+\n"; 
			}//end_print()
			
			void print(){
				std::cout << "+-----------------------------------+\n";
				std::cout << "Memory::print() [Ascii 0-255]\n\n";
				for(int i=0;i<v_chars.size();i++){
					std::cout << "\tBytes[" << i << "] : " << (int)static_cast<uint8_t>(v_chars[i]) << "\n";
				}//endfor
				std::cout << "+-----------------------------------+\n"; 
			}
			void assign(const char* ptr,size_t n){
				v_chars.assign(ptr,ptr+n);
			}//end_allcate
			const char* ptr(){
				return v_chars.data();
			}

			std::vector<char>& ref(){
				return v_chars;
			}
			char& operator[](const int &i){
				return v_chars[i];
			}//end_operator

			size_t size(){
				return v_chars.size();
			}

			std::string makeStr(){
				std::string tmp;
				for(int i=0;i<v_chars.size();i++){
					tmp.push_back(v_chars[i]);
				}//endfor
				return tmp;
			}//end

			void clear(){
				v_chars.clear();
			}//end_clear

			~Memory(){
				v_chars.clear();
			};
	//==========================================
	};
	//==========================================
};


#endif