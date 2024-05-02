# Meta Package
Name:           ros-humble-demo-nodes-cpp-native
Version:        0.20.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-demo_nodes_cpp_native and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-demo_nodes_cpp_native
Requires:       ros2-humble-demo_nodes_cpp_native-devel

Obsoletes: ros-humble-demo-nodes-cpp-native < 0.20.3-1

%description
C++ nodes which access the native handles of the rmw implementation.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- Initial humble build
