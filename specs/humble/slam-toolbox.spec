# Meta Package
Name:           ros-humble-slam-toolbox
Version:        2.6.8
Release:        1%{?dist}
License:        LGPL
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-slam_toolbox and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-slam_toolbox
Requires:       ros2-humble-slam_toolbox-devel

Obsoletes: ros-humble-slam-toolbox < 2.6.8-1

%description
This package provides a sped up improved slam karto with updated SDK
and visualization and modification toolsets

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.8-1
- Update to latest release
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.6-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.5-1
- update to latest upstream release
* Thu Aug 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.5-1
- update to latest upstream
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.4-1
- update to latest release
