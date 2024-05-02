# Meta Package
Name:           ros-humble-tlsf
Version:        0.7.0
Release:        1%{?dist}
License:        GNU Lesser Public License 2.1
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-tlsf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tlsf
Requires:       ros2-humble-tlsf-devel

Obsoletes: ros-humble-tlsf < 0.7.0-1

%description
TLSF allocator version 2.4.6

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.7.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.7.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.7.0-1
- Initial humble build
