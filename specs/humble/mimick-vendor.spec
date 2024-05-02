# Meta Package
Name:           ros-humble-mimick-vendor
Version:        0.2.8
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/Snaipe/Mimick
Summary:        Meta package for ros2-humble-mimick_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-mimick_vendor
Requires:       ros2-humble-mimick_vendor-devel

Obsoletes: ros-humble-mimick-vendor < 0.2.8-1

%description
Wrapper around mimick, it provides an ExternalProject build of mimick.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.8-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.8-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.8-1
- Initial humble build
