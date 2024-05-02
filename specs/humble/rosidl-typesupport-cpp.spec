# Meta Package
Name:           ros-humble-rosidl-typesupport-cpp
Version:        2.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rosidl_typesupport_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rosidl_typesupport_cpp
Requires:       ros2-humble-rosidl_typesupport_cpp-devel

Obsoletes: ros-humble-rosidl-typesupport-cpp < 2.0.1-1

%description
Generate the type support for C++ messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.1-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.1-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.0-1
- Initial humble build
