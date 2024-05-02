# Meta Package
Name:           ros-humble-behaviortree-cpp-v3
Version:        3.8.6
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-behaviortree_cpp_v3 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-behaviortree_cpp_v3
Requires:       ros2-humble-behaviortree_cpp_v3-devel

Obsoletes: ros-humble-behaviortree-cpp-v3 < 3.8.6-1

%description
This package provides the Behavior Trees core library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.8.6-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.8.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.8.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.8.5-1
- update to latest upstream release
* Fri Jun 30 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.8.4-1
- update to latest upstream release
* Mon Apr 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.8.3-1
- update to latest upsteam
