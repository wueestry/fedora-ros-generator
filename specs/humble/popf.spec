# Meta Package
Name:           ros-humble-popf
Version:        0.0.14
Release:        1%{?dist}
License:        GPLv2
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-popf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-popf
Requires:       ros2-humble-popf-devel

Obsoletes: ros-humble-popf < 0.0.14-1

%description
The POPF package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Nov 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.14-1
- update to latest release
* Thu Apr 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.14-1
- update to latest release
