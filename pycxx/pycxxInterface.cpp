

#include"pycxxBuffer.hpp"
//============================================================
namespace pycxx{
	namespace buffer{
		Pointer iPtr;
		Memory oMemory;
	};
	void main();

};
//=========================================
// source from c++projects 
#include "main.hpp" 
//=========================================


#ifdef __PYCXX_PURECXX_DEBUG__
	// PURECXX Debug
	int main(){
		pycxx::main();
		return 0;
	}//end_return

#else 

	// ctypes :
	extern "C"{
		const char* passBytes(const char* bytes,size_t numBytes){
			pycxx::buffer::iPtr.set(bytes,numBytes);
			pycxx::main();
			return pycxx::buffer::oMemory.ptr(); 	
		}//end_main

		size_t passBytesSize(){
			return pycxx::buffer::oMemory.size();
		}

	};
#endif

