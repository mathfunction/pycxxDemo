#ifdef cxxProjects_passDataFrame

	#include <iostream>
	#include "json.hpp"

	void pycxx::main(){
		#ifndef __PYCXX_PURECXX_DEBUG__
			nlohmann::json j = nlohmann::json::parse(pycxx::buffer::iPtr.data());
			std::cout << j << std::endl;
			



			std::string o = j.dump();
			pycxx::buffer::oMemory.assign(o.data(),o.size());
		#endif
		
	}//end_mainRoutine


#endif