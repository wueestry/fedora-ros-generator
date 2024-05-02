# Meta Package
Name:           ros-humble-rosidl-typesupport-interface
Version:        3.1.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rosidl_typesupport_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rosidl_typesupport_interface
Requires:       ros2-humble-rosidl_typesupport_interface-devel

Obsoletes: ros-humble-rosidl-typesupport-interface < 3.1.5-1

%description
The interface for rosidl typesupport packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.5-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.5-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.4-1
- Initial humble build
