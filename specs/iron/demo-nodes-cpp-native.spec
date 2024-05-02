# Meta Package
Name:           ros-iron-demo-nodes-cpp-native
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-demo_nodes_cpp_native and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-demo_nodes_cpp_native
Requires:       ros2-iron-demo_nodes_cpp_native-devel

Obsoletes: ros-iron-demo-nodes-cpp-native < 0.27.1-1

%description
C++ nodes which access the native handles of the rmw implementation.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
